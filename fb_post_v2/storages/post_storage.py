from typing import Optional, List, Dict

from django.db.models import Count, Q, F

from fb_post_v2.interactors.storages.post_storage import GetPostDTO, \
    CommentDTO, UserReactionDTO, TotalReactionCountDTO, ReactionDTO, \
    PostStorage, ReplyDTO, UserDTO, ReactionCountDTO, PostDTO, ReactionStatsDTO, \
    CommentWithRepliesDTO, UserPostsDTO
from fb_post_v2.models.models import Post, PostReaction, Comment, \
    CommentReaction


class PostStorage(PostStorage):

    def get_comment_id(self, comment_id: int) -> int:
        reply = Comment.objects.get(id=comment_id)
        comment = Comment.objects.get(id=reply.commented_on_id)
        return comment.id

    def create_post(self, post_content: str, created_by: int) -> int:
        post = Post.objects.create(user_id=created_by,
                                   post_description=post_content)

        return post.id

    def get_all_comment_replies_dict(self, replies):
        comment_replies = {}
        for reply in replies:
            try:
                comment_replies[reply['commented_on_id']].append(reply)
            except:
                comment_replies[reply['commented_on_id']] = [reply]

        return comment_replies

    def get_all_comment_reactions_dict(self, all_comment_reactions):
        comment_reactions = {}
        for reaction in all_comment_reactions:
            try:
                comment_reaction = comment_reactions[reaction['comment_id']]
                comment_reaction['count'] += 1
                comment_reaction['types'].add(reaction['reaction'])
            except:
                comment_reactions[reaction['comment_id']] = {'count': 1,
                                                             'types': {
                                                                 reaction[
                                                                     'reaction']}}

        return comment_reactions

    def get_commenter_dto(self, comment):

        return UserDTO(user_id=comment['user_id'],
                       username=comment['user__username'],
                       profile_pic=comment['user__profile_pic'])

    def get_comment_reactions_dto(self, comment_id, comment_reactions):
        try:
            comment_reaction_dto = ReactionStatsDTO(
                count=comment_reactions[comment_id]['count'],
                types=list(comment_reactions[comment_id]['types']))
        except:
            comment_reaction_dto = ReactionStatsDTO(count=0, types=[])

        return comment_reaction_dto

    def get_all_replies_for_comment(self, comment_replies, comment):
        try:
            all_replies = comment_replies[comment['id']]
            replies_count = len(all_replies)
        except:
            all_replies = []
            replies_count = 0

        return all_replies, replies_count

    def get_comment_dto(self, comment, comment_reactions):
        comment_user_dto = self.get_commenter_dto(comment)
        comment_reaction_dto = self.get_comment_reactions_dto(comment['id'],
                                                              comment_reactions)

        return CommentDTO(id=comment['id'], user=comment_user_dto,
                          comment_content=comment['message'],
                          comment_create_date=comment['comment_create_date'],
                          comment_reactions=comment_reaction_dto)

    def get_comment_with_replies_dto(self, comment, comment_reactions,
                                     replies_count, replies_dto):
        comment_user_dto = self.get_commenter_dto(comment)
        comment_reaction_dto = self.get_comment_reactions_dto(comment['id'],
                                                              comment_reactions)

        return CommentWithRepliesDTO(id=comment['id'], user=comment_user_dto,
                                     comment_content=comment['message'],
                                     comment_create_date=
                                     comment['comment_create_date'],
                                     comment_reactions=comment_reaction_dto,
                                     replies_count=replies_count,
                                     replies=replies_dto)

    def get_replies_dto_list(self, all_replies, comment_reactions):
        replies_dto_list = []
        for reply in all_replies:
            reply_dto = self.get_comment_dto(reply, comment_reactions)
            replies_dto_list.append(reply_dto)

        return replies_dto_list

    def get_comments_dto_list(self, post_comments, comment_replies,
                              comment_reactions):

        comments_dto_list = []
        for comment in post_comments:
            all_replies, replies_count = self.get_all_replies_for_comment(
                comment_replies, comment)

            replies_dto_list = self.get_replies_dto_list(all_replies,
                                                         comment_reactions)

            comment_dto = self.get_comment_with_replies_dto(comment,
                                                            comment_reactions,
                                                            replies_count,
                                                            replies_dto_list)
            comments_dto_list.append(comment_dto)

        return comments_dto_list

    def get_post(self, post_id: int) -> GetPostDTO:
        post = Post.objects.get(id=post_id)
        post_dto = PostDTO(id=post.id, post_content=post.post_description,
                           post_create_date=post.post_create_date)
        post_user_dto = UserDTO(user_id=post.user_id,
                                username=post.user.username,
                                profile_pic=post.user.profile_pic)

        post_reactions = PostReaction.objects.filter(
            post_id=post_id).values_list('reaction', flat=True)
        post_reaction_count = post_reactions.count()
        post_reaction_type = post_reactions.distinct()

        post_reaction_dto = ReactionStatsDTO(count=post_reaction_count,
                                            types=list(post_reaction_type))

        post_comments = Comment.objects.filter(post_id=post_id,
                                               commented_on_id=None).values(
            'id', 'user_id',
            'user__username',
            'user__profile_pic',
            'commented_on_id',
            'comment_create_date',
            'message')

        comments_ids = [comment['id'] for comment in post_comments]

        replies = Comment.objects.filter(
            commented_on_id__in=comments_ids).values('id', 'user_id',
                                                     'user__username',
                                                     'user__profile_pic',
                                                     'commented_on_id',
                                                     'comment_create_date',
                                                     'message')

        comment_replies = self.get_all_comment_replies_dict(replies)

        comments_ids.extend([reply['id'] for reply in replies])

        all_comment_reactions = CommentReaction.objects.filter(
            comment_id__in=comments_ids).values('comment_id',
                                                'reaction')
        comment_reactions = self.get_all_comment_reactions_dict(
            all_comment_reactions)

        comments_dto_list = self.get_comments_dto_list(post_comments,
                                                       comment_replies,
                                                       comment_reactions)

        return GetPostDTO(post=post_dto, posted_by=post_user_dto,
                          reactions=post_reaction_dto,
                          comments=comments_dto_list,
                          comment_count=len(post_comments))

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
                                   comment_create_date=reply.comment_create_date)

            replies_list.append(replies_dto)

        return replies_list

    def get_user_posts(self, user_id: int, offset: int,
                       limit: int) -> UserPostsDTO:

        user_posts = Post.objects.filter(user_id=user_id)[
                     offset: offset + limit]
        posts_dto = [self.get_post(post_id=post.id) for post in user_posts]

        return UserPostsDTO(posts=posts_dto)

    def get_post_reactions(self, post_id: int, offset: int, limit: int) -> List[
                                                                UserReactionDTO]:

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
        positive_posts = PostReaction.objects.values('post').annotate(
            positive_count=Count('reaction', filter=Q(
                reaction__in=("LIKE", "LOVE", "WOW", "HAHA"))),
            negative_count=Count('reaction', filter=Q(
                reaction__in=("SAD", "ANGRY")))).filter(
            positive_count__gt=F('negative_count')).values('post_id')

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
        except:
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
