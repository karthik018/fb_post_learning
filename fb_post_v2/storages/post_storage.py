from typing import Optional, List, Dict

from django.db.models import Count, Q, F

from fb_post_v2.interactors.storages.post_storage import PostIdDTO, GetPostDTO, CommentIdDTO, ReactionIdDTO, CommentDTO, \
    UserPosts, ReactionDetailsDTO, TotalReactionDTO, ReactionDTO, PostStorage, RepliesDTO, UserDTO, \
    ReactionCountDTO, PostDTO, ReactionsDTO, CommentWithRepliesDTO
from fb_post_v2.models.models import *


class PostStorage(PostStorage):

    def get_comment_id(self, comment_id: int) -> CommentIdDTO:
        reply = Comment.objects.get(id=comment_id)
        comment = Comment.objects.get(id=reply.commented_on_id)
        return CommentIdDTO(comment_id=comment.id)

    def create_post(self, post_content: str, created_by: int) -> PostIdDTO:
        post = Post.objects.create(user_id=created_by, post_description=post_content)
        return PostIdDTO(post_id=post.id)

    def get_post(self, post_id: int) -> GetPostDTO:
        post = Post.objects.get(id=post_id)
        post_dto = PostDTO(id=post.id, post_content=post.post_description, post_create_date=post.post_create_date)
        post_user_dto = UserDTO(user_id=post.user_id, username=post.user.username, profile_pic=post.user.profile_pic)

        post_reactions = PostReaction.objects.filter(post_id=post_id).values_list('reaction', flat=True)
        post_reaction_count = post_reactions.count()
        post_reaction_type = post_reactions.distinct()

        post_reaction_dto = ReactionsDTO(count=post_reaction_count, types=list(post_reaction_type))

        post_comments = Comment.objects.filter(post_id=post_id, commented_on_id=None).values('id', 'user_id', 'user__username', 'user__profile_pic', 'commented_on_id', 'comment_create_date', 'message')

        comments_ids = [comment['id'] for comment in post_comments]

        replies = Comment.objects.filter(commented_on_id__in=comments_ids).values('id', 'user_id','user__username','user__profile_pic','commented_on_id','comment_create_date','message')
        comment_replies = {}
        for reply in replies:
            try:
                comment_replies[reply['commented_on_id']].append(reply)
            except:
                comment_replies[reply['commented_on_id']] = [reply]

        comments_ids[len(comments_ids) + 1:] = [reply['id'] for reply in replies]
        all_comment_reactions = CommentReaction.objects.filter(comment_id__in=comments_ids).values('comment_id',
                                                                                                   'reaction')

        comment_reactions = {}
        for reaction in all_comment_reactions:
            try:
                comment_reaction = comment_reactions[reaction['comment_id']]
                comment_reaction['count'] += 1
                comment_reaction['types'].add(reaction['reaction'])
            except:
                comment_reactions[reaction['comment_id']] = {'count': 1, 'types': set([reaction['reaction']])}

        comments_dto = []
        for comment in post_comments:
            comment_user_dto = UserDTO(user_id=comment['user_id'], username=comment['user__username'],
                                       profile_pic=comment['user__profile_pic'])
            try:
                comment_reaction_dto = ReactionsDTO(count=comment_reactions[comment['id']]['count'],
                                                    types=list(comment_reactions[comment['id']]['types']))
            except:
                comment_reaction_dto = ReactionsDTO(count=0, types=[])
            try:
                all_replies = comment_replies[comment['id']]
                replies_count = len(all_replies)
            except:
                all_replies = []
                replies_count = 0

            replies_dto = []
            for reply in all_replies:
                reply_user_dto = UserDTO(user_id=reply['user_id'], username=reply['user__username'],
                                         profile_pic=reply['user__profile_pic'])
                reply_reaction_dto = ReactionsDTO(count=comment_reactions[reply['id']]['count'],
                                                  types=list(comment_reactions[reply['id']]['types']))
                reply_dto = CommentDTO(id=reply['id'], user=reply_user_dto, comment_content=reply['message'],
                                       comment_create_date=reply['comment_create_date'],
                                       comment_reactions=reply_reaction_dto)
                replies_dto.append(reply_dto)

            comment_dto = CommentWithRepliesDTO(id=comment['id'], user=comment_user_dto,
                                                comment_content=comment['message'],
                                                comment_create_date=comment['comment_create_date'],
                                                comment_reactions=comment_reaction_dto,
                                                replies_count=replies_count,
                                                replies=replies_dto)
            comments_dto.append(comment_dto)

        return GetPostDTO(post=post_dto, posted_by=post_user_dto, reactions=post_reaction_dto,
                          comments=comments_dto, comment_count=len(post_comments))

    def create_comment(self, post_id: int, commenter: int, comment_content: str) -> CommentIdDTO:
        comment = Comment.objects.create(post_id=post_id, user_id=commenter, message=comment_content)
        return CommentIdDTO(comment_id=comment.id)

    def check_comment_or_reply(self, comment_id: int) -> bool:
        comment = Comment.objects.get(id=comment_id)
        if comment.commented_on is not None:
            return False
        return True

    def create_reply(self, comment_id: int, commenter: int, comment_content: str) -> CommentIdDTO:
        comment = Comment.objects.get(id=comment_id)
        reply = Comment.objects.create(post_id=comment.post_id, user_id=commenter, commented_on_id=comment.id,
                                       message=comment_content)
        return CommentIdDTO(comment_id=reply.id)

    def react_to_post(self, post_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        reaction = PostReaction.objects.create(post_id=post_id, user_id=reacted_by, reaction=reaction_type)
        return ReactionIdDTO(reaction_id=reaction.id)

    def react_to_comment(self, comment_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        reaction = CommentReaction.objects.create(comment_id=comment_id, user_id=reacted_by, reaction=reaction_type)
        return ReactionIdDTO(reaction_id=reaction.id)

    def get_comment_replies(self, comment_id: int, offset: int, limit: int) -> List[RepliesDTO]:
        replies = Comment.objects.filter(commented_on_id=comment_id)[offset: offset+limit]
        replies_list = []
        for reply in replies:
            userdto = UserDTO(user_id=reply.user_id, username=reply.user.username,
                              profile_pic=reply.user.profile_pic)
            replies_dto = RepliesDTO(comment_id=reply.id, user=userdto, comment_content=reply.message,
                                     comment_create_date=reply.comment_create_date)
            replies_list.append(replies_dto)
        return replies_list

    def get_user_posts(self, user_id: int, offset: int, limit: int) -> UserPosts:
        user_posts = Post.objects.filter(user_id=user_id)[offset: offset+limit]
        posts_dto = [self.get_post(post_id=post.id) for post in user_posts]
        return UserPosts(posts=posts_dto)

    def get_reactions_to_post(self, post_id: int, offset: int, limit: int) -> List[ReactionDetailsDTO]:
        post_reactions = PostReaction.objects.filter(post_id=post_id)[offset: offset+limit]
        reactions_list = [ReactionDetailsDTO(user_id=post.user_id, username=post.user.username,
                                             profile_pic=post.user.profile_pic, reaction=post.reaction)
                          for post in post_reactions]
        return reactions_list

    def get_posts_reacted_by_user(self, user_id: int) -> List[PostIdDTO]:
        posts = PostReaction.objects.filter(user_id=user_id)
        posts_list = [PostIdDTO(post_id=post.post_id) for post in posts]
        return posts_list

    def get_posts_with_more_positive_reactions(self) -> List[PostIdDTO]:
        positive_posts = PostReaction.objects.values('post').annotate(
            positive_count=Count('reaction', filter=Q(reaction__in=("LIKE", "LOVE", "WOW", "HAHA"))),
            negative_count=Count('reaction', filter=Q(reaction__in=("SAD", "ANGRY")))).filter(
            positive_count__gt=F('negative_count')).values('post_id')

        posts_lists = [PostIdDTO(post_id=post['post_id']) for post in positive_posts]
        return posts_lists

    def get_reaction_metrics(self, post_id: int) -> List[ReactionCountDTO]:
        likes = PostReaction.objects.filter(post_id=post_id).values('reaction').annotate(react_count=Count('reaction'))
        reaction_metrics = [ReactionCountDTO(count=like['react_count'], reaction=like['reaction'])
                            for like in likes]
        return reaction_metrics

    def get_total_reaction_count(self) -> TotalReactionDTO:
        reactions_count = PostReaction.objects.count()
        return TotalReactionDTO(count=reactions_count)

    def delete_post(self, post_id) -> PostIdDTO:
        post = Post.objects.get(id=post_id)
        post.delete()
        return PostIdDTO(post_id=post.id)

    def post_exists(self, post_id) -> bool:
        try:
            Post.objects.get(id=post_id)
            return True
        except:
            return False

    def post_reaction_exists(self, post_id: int, reacted_by: int) -> ReactionDTO:
        reaction = PostReaction.objects.get(post_id=post_id, user_id=reacted_by)
        return ReactionDTO(id=reaction.id, react_on_id=reaction.post_id, reacted_by=reaction.user_id,
                           reaction=reaction.reaction)

    def delete_post_reaction(self, post_id: int, reacted_by: int) -> ReactionIdDTO:
        reaction = PostReaction.objects.get(post_id=post_id, user_id=reacted_by)
        reaction.delete()
        return ReactionIdDTO(reaction_id=reaction.id)

    def update_post_reaction(self, post_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        reaction = PostReaction.objects.get(post_id=post_id, user_id=reacted_by)
        reaction.reaction = reaction_type
        reaction.save()
        return ReactionIdDTO(reaction_id=reaction.id)

    def comment_reaction_exists(self, comment_id: int, reacted_by: int) -> ReactionDTO:
        reaction = CommentReaction.objects.get(comment_id=comment_id, user_id=reacted_by)
        return ReactionDTO(id=reaction.id, react_on_id=reaction.comment_id, reacted_by=reaction.user_id,
                           reaction=reaction.reaction)

    def delete_comment_reaction(self, comment_id: int, reacted_by: int) -> ReactionIdDTO:
        reaction = CommentReaction.objects.get(comment_id=comment_id, user_id=reacted_by)
        reaction.delete()
        return ReactionIdDTO(reaction_id=reaction.id)

    def update_comment_reaction(self, comment_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        reaction = CommentReaction.objects.get(comment_id=comment_id, user_id=reacted_by)
        reaction.reaction = reaction_type
        reaction.save()
        return ReactionIdDTO(reaction_id=reaction.id)
