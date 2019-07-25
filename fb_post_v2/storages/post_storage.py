from typing import Optional, List, Dict

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q, F

from fb_post_v2.interactors.storages.post_storage import GetPostDTO, \
    CommentDTO, UserReactionDTO, TotalReactionCountDTO, ReactionDTO, \
    PostStorage, ReplyDTO, UserDTO, ReactionCountDTO, PostDTO, \
    ReactionStatsDTO, UserPostsDTO
from fb_post_v2.models.models import Post, PostReaction, Comment, \
    CommentReaction, User


class Storage(PostStorage):

    def get_comment_id(self, reply_id: int) -> int:
        reply = Comment.objects.get(id=reply_id)
        comment = Comment.objects.get(id=reply.commented_on_id)
        return comment.id

    def create_post(self, post_content: str, created_by: int) -> int:
        post = Post.objects.create(user_id=created_by,
                                   post_description=post_content)

        return post.id

    @staticmethod
    def get_comment_wise_reactions_dict(all_comment_reactions):
        comment_reactions = {}
        for reaction in all_comment_reactions:
            try:
                comment_reaction = comment_reactions[reaction['comment_id']]
                comment_reaction['count'] += 1
                comment_reaction['types'].add(reaction['reaction'])
            except KeyError:
                comment_reactions[reaction['comment_id']] = {
                    'count': 1,
                    'types': {reaction['reaction']}
                }

        return comment_reactions

    @staticmethod
    def get_comments_reaction_stats_dtos(comment_reactions):
        reactions = {}
        for comment_id in comment_reactions:
            comment_reaction_dto = ReactionStatsDTO(
                count=comment_reactions[comment_id]['count'],
                types=list(comment_reactions[comment_id]['types']))

            reactions[comment_id] = comment_reaction_dto

        return reactions

    @staticmethod
    def get_all_comment_dtos_list(comments):
        comments_list = []
        for comment in comments:
            comment_dto = CommentDTO(
                id=comment.id, user_id=comment.user_id,
                commented_on_id=comment.commented_on_id,
                comment_content=comment.message,
                comment_create_date=comment.comment_create_date)

            comments_list.append(comment_dto)

        return comments_list

    @staticmethod
    def get_all_user_dtos_list(post_id, post_user_id):
        all_user_ids = [post_user_id]
        comment_users = Comment.objects.filter(post_id=post_id).values_list(
                                                'user', flat=True)
        all_user_ids.extend(comment_users)
        all_user_ids = list(set(all_user_ids))

        users = User.objects.filter(id__in=all_user_ids)

        users_dtos = []
        for user in users:
            users_dtos.append(UserDTO(user_id=user.id,
                                      username=user.username,
                                      profile_pic=user.profile_pic))

        return users_dtos

    def get_post(self, post_id: int) -> GetPostDTO:
        comments = []
        post = Post.objects.get(id=post_id)
        post_dto = PostDTO(id=post.id, user_id=post.user_id,
                           post_content=post.post_description,
                           post_create_date=post.post_create_date)

        post_reactions = PostReaction.objects.filter(post_id=post_id) \
            .values_list('reaction', flat=True)

        post_reaction_count = post_reactions.count()
        post_reaction_type = post_reactions.distinct()

        post_reaction_dto = ReactionStatsDTO(count=post_reaction_count,
                                             types=list(post_reaction_type))

        post_comments = Comment.objects.filter(post_id=post_id)

        comments.extend(self.get_all_comment_dtos_list(post_comments))

        comments_ids = [comment.id for comment in post_comments]

        all_comment_reactions = CommentReaction.objects.filter(
            comment_id__in=comments_ids).values('comment_id', 'reaction')

        comment_reactions = self.get_comment_wise_reactions_dict(
            all_comment_reactions)

        comment_reactions = self.get_comments_reaction_stats_dtos(
            comment_reactions)

        all_users = self.get_all_user_dtos_list(post_id, post_dto.user_id)

        return GetPostDTO(post=post_dto, post_reactions=post_reaction_dto,
                          comments=comments,
                          comment_reactions=comment_reactions,
                          all_users=all_users)

    def create_comment(self, post_id: int, commenter: int,
                       comment_content: str) -> int:
        comment = Comment.objects.create(post_id=post_id, user_id=commenter,
                                         message=comment_content)

        return comment.id

    def is_comment_or_reply(self, comment_id: int) -> bool:
        comment = Comment.objects.get(id=comment_id)

        if comment.commented_on is not None:
            return False

        return True

    def create_reply(self, comment_id: int, commenter: int,
                     comment_content: str) -> int:

        comment = Comment.objects.get(id=comment_id)

        reply = Comment.objects.create(post_id=comment.post_id,
                                       user_id=commenter,
                                       commented_on_id=comment.id,
                                       message=comment_content)

        return reply.id

    def add_post_reaction(self, post_id: int, reacted_by: int,
                          reaction_type: str) -> int:
        reaction = PostReaction.objects.create(post_id=post_id,
                                               user_id=reacted_by,
                                               reaction=reaction_type)
        return reaction.id

    def add_comment_reaction(self, comment_id: int, reacted_by: int,
                             reaction_type: str) -> int:

        reaction = CommentReaction.objects.create(comment_id=comment_id,
                                                  user_id=reacted_by,
                                                  reaction=reaction_type)

        return reaction.id

    def get_comment_replies(self, comment_id: int, offset: int, limit: int) -> \
            List[ReplyDTO]:

        replies = Comment.objects.filter(commented_on_id=comment_id)[
                  offset: offset + limit]

        replies_list = []
        for reply in replies:
            userdto = UserDTO(user_id=reply.user_id,
                              username=reply.user.username,
                              profile_pic=reply.user.profile_pic)

            replies_dto = ReplyDTO(comment_id=reply.id, user=userdto,
                                   comment_content=reply.message,
                                   comment_create_date=reply.comment_create_date
                                   )

            replies_list.append(replies_dto)

        return replies_list

    def get_user_posts(self, user_id: int, offset: int,
                       limit: int) -> UserPostsDTO:

        user_posts = Post.objects.filter(user_id=user_id)[
                     offset: offset + limit]
        posts_dto = [self.get_post(post_id=post.id) for post in user_posts]

        return UserPostsDTO(posts=posts_dto)

    def get_post_reactions(self, post_id: int, offset: int, limit: int) -> \
            List[UserReactionDTO]:

        post_reactions = PostReaction.objects.filter(post_id=post_id)[
                         offset: offset + limit]
        reactions_list = [
            UserReactionDTO(user_id=post.user_id, username=post.user.username,
                            profile_pic=post.user.profile_pic,
                            reaction=post.reaction)
            for post in post_reactions]

        return reactions_list

    def get_user_reacted_posts(self, user_id: int) -> List[int]:
        posts = PostReaction.objects.filter(user_id=user_id)
        posts_list = [post.post_id for post in posts]

        return posts_list

    def get_positive_reaction_posts(self) -> List[int]:
        positive_reactions_filter = Q(reaction__in=("LIKE", "LOVE", "WOW",
                                                    "HAHA"))

        negative_reactions_filter = Q(reaction__in=("SAD", "ANGRY"))

        positive_posts = PostReaction.objects.values('post').annotate(
            positive_count=Count('reaction', filter=positive_reactions_filter),
            negative_count=Count('reaction', filter=negative_reactions_filter))\
            .filter(positive_count__gt=F('negative_count')).values('post_id')

        posts_lists = [post['post_id'] for post in positive_posts]

        return posts_lists

    def get_reaction_metrics(self, post_id: int) -> List[ReactionCountDTO]:

        likes = PostReaction.objects.filter(post_id=post_id).values(
            'reaction').annotate(react_count=Count('reaction'))
        reaction_metrics = [ReactionCountDTO(count=like['react_count'],
                                             reaction=like['reaction'])
                            for like in likes]

        return reaction_metrics

    def get_total_reaction_count(self) -> TotalReactionCountDTO:
        reactions_count = PostReaction.objects.count()

        return TotalReactionCountDTO(count=reactions_count)

    def delete_post(self, post_id) -> Optional[int]:
        post = Post.objects.get(id=post_id)
        post.delete()

        return post.id

    def post_exists(self, post_id) -> bool:
        try:
            Post.objects.get(id=post_id)
            return True
        except ObjectDoesNotExist:
            return False

    def post_reaction_exists(self, post_id: int,
                             reacted_by: int) -> ReactionDTO:

        reaction = PostReaction.objects.get(post_id=post_id, user_id=reacted_by)

        return ReactionDTO(id=reaction.id, react_on_id=reaction.post_id,
                           reacted_by=reaction.user_id,
                           reaction=reaction.reaction)

    def delete_post_reaction(self, post_id: int,
                             reacted_by: int) -> Optional[int]:
        reaction = PostReaction.objects.get(post_id=post_id, user_id=reacted_by)
        reaction.delete()

        return reaction.id

    def update_post_reaction(self, post_id: int, reacted_by: int,
                             reaction_type: str) -> int:
        reaction = PostReaction.objects.get(post_id=post_id, user_id=reacted_by)
        reaction.reaction = reaction_type
        reaction.save()

        return reaction.id

    def comment_reaction_exists(self, comment_id: int,
                                reacted_by: int) -> ReactionDTO:
        reaction = CommentReaction.objects.get(comment_id=comment_id,
                                               user_id=reacted_by)

        return ReactionDTO(id=reaction.id, react_on_id=reaction.comment_id,
                           reacted_by=reaction.user_id,
                           reaction=reaction.reaction)

    def delete_comment_reaction(self, comment_id: int,
                                reacted_by: int) -> Optional[int]:
        reaction = CommentReaction.objects.get(comment_id=comment_id,
                                               user_id=reacted_by)
        reaction.delete()

        return reaction.id

    def update_comment_reaction(self, comment_id: int, reacted_by: int,
                                reaction_type: str) -> int:
        reaction = CommentReaction.objects.get(comment_id=comment_id,
                                               user_id=reacted_by)
        reaction.reaction = reaction_type
        reaction.save()

        return reaction.id
