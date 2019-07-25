from typing import List, Optional

from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import TotalReactionCountDTO,\
    ReactionCountDTO, UserReactionDTO, ReplyDTO, GetPostDTO, UserDTO, \
    ReactionStatsDTO, CommentDTO, CommentWithRepliesDTO, UserPostsDTO


class JsonPresenter(JsonPresenter):

    def get_create_post_response(self, post_id: int) -> dict:
        return {"postid": post_id}

    def get_user_dict(self, user_dto: UserDTO) -> dict:
        return {"userid": user_dto.user_id,
                "username": user_dto.username,
                "profile_pic": user_dto.profile_pic}

    def get_datetime_string(self, datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")

    def get_reactions_dict(self, reactions_dto: ReactionStatsDTO) -> dict:
        return {"count": reactions_dto.count,
                "types": reactions_dto.types}

    def get_reply_dict(self, reply: CommentDTO) -> dict:
        return {"comment_id": reply.id,
                "commenter": self.get_user_dict(reply.user),
                "comment_message": reply.comment_content,
                "comment_create_date": self.get_datetime_string(
                    reply.comment_create_date),
                "reactions": self.get_reactions_dict(reply.comment_reactions)}

    def get_comment_dict(self, comment: CommentWithRepliesDTO,
                         replies: List) -> dict:

        return {"comment_id": comment.id,
                "commenter": self.get_user_dict(comment.user),
                "comment_message": comment.comment_content,
                "comment_create_date": self.get_datetime_string(
                    comment.comment_create_date),
                "reactions": self.get_reactions_dict(comment.comment_reactions),
                "replies_count": comment.replies_count, "replies": replies}

    def get_post_response(self, get_post_dto: GetPostDTO):

        comments = []
        for comment in get_post_dto.comments:
            replies = []
            for reply in comment.replies:
                comment_reply = self.get_reply_dict(reply)
                replies.append(comment_reply)
            post_comment = self.get_comment_dict(comment, replies)
            comments.append(post_comment)

        post = {"postid": get_post_dto.post.id,
                "posted_by": self.get_user_dict(get_post_dto.posted_by),
                "post_content": get_post_dto.post.post_content,
                "post_create_date": self.get_datetime_string(
                    get_post_dto.post.post_create_date),
                "reactions": self.get_reactions_dict(get_post_dto.reactions),
                "comment_count": get_post_dto.comment_count,
                "comments": comments}

        return post

    def get_create_comment_response(self, comment_id: int):
        return {"comment_id": comment_id}

    def get_create_reply_response(self, reply_id: int):
        return {"reply_id": reply_id}

    def get_add_post_reaction_response(self, reaction_id: int):
        return {"reactionid": reaction_id}

    def get_add_comment_reaction_response(self, reaction_id: int):
        return {"reactionid": reaction_id}

    def get_comment_replies_response(self, replies_dto: List[ReplyDTO]):
        replies = []
        for reply_dto in replies_dto:
            reply = {"comment_id": reply_dto.comment_id,
                     "commenter": self.get_user_dict(reply_dto.user),
                     "comment_create_date": self.get_datetime_string(
                         reply_dto.comment_create_date),
                     "comment_message": reply_dto.comment_content}
            replies.append(reply)

        return {"replies": replies}

    def get_user_posts_response(self, posts_dto: UserPostsDTO):
        user_posts = [self.get_post_response(get_post_dto)
                      for get_post_dto in posts_dto.posts]

        return {"posts": user_posts}

    def get_post_reactions_response(self, reactions_dto: List[UserReactionDTO]):
        reactions = []
        for reaction_dto in reactions_dto:
            reaction = self.get_user_dict(reaction_dto)
            reaction["reaction"] = reaction_dto.reaction
            reactions.append(reaction)

        return {"reactions": reactions}

    def get_user_reacted_posts_response(self, post_ids: List[int]):
        posts = []
        for post_id in post_ids:
            post = {"postid": post_id}
            posts.append(post)

        return {"posts": posts}

    def get_positive_reaction_posts_response(self, post_ids: List[int]):
        posts = []
        for post_id in post_ids:
            post = {"postid": post_id}
            posts.append(post)

        return {"posts": posts}

    def get_reaction_metrics_response(self,
                                      reactions_dto: List[ReactionCountDTO]):
        reactions = []
        for reaction_dto in reactions_dto:
            reaction_metric = {"count": reaction_dto.count,
                               "reaction": reaction_dto.reaction}
            reactions.append(reaction_metric)

        return {"reactions": reactions}

    def get_total_reaction_count_response(self,
                                          count_dto: TotalReactionCountDTO):

        return {"total_count": count_dto.count}

    def get_delete_post_response(self, post_id: Optional[int]):
        return {"post_id": post_id}

    def post_not_exists(self):
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid post id', 'INVALID_POST_ID')

    def raise_not_comment(self):
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid comment id', 'INVALID_COMMENT_ID')
