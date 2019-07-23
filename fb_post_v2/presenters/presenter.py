from typing import List

from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostIdDTO, TotalReactionDTO, ReactionCountDTO, \
    ReactionDetailsDTO, UserPosts, RepliesDTO, ReactionIdDTO, CommentIdDTO, GetPostDTO


class JsonPresenter(JsonPresenter):
    def create_post(self, post_dto: PostIdDTO):
        return {"postid": post_dto.post_id}

    def get_reply_data(self, reply):
        return {"comment_id": reply.id, "commenter": {"user_id": reply.user.user_id,
                                                      "username": reply.user.username,
                                                      "profile_pic": reply.user.profile_pic},
                "comment_message": reply.comment_content,
                "comment_create_date": reply.comment_create_date.strftime("%Y-%m-%d %H:%M:%S"),
                "reactions": {"count": reply.comment_reactions.count,
                              "types": reply.comment_reactions.types}}

    def get_comment_data(self, comment, replies):
        return {"comment_id": comment.id, "commenter": {"userid": comment.user.user_id,
                                                        "username": comment.user.username,
                                                        "profile_pic": comment.user.profile_pic},
                "comment_message": comment.comment_content,
                "comment_create_date": comment.comment_create_date.strftime("%Y-%m-%d %H:%M:%S"),
                "reactions": {"count": comment.comment_reactions.count,
                              "types": comment.comment_reactions.types},
                "replies_count": comment.replies_count, "replies": replies}

    def get_post(self, get_post_dto: GetPostDTO):

        comments = []
        for comment in get_post_dto.comments:
            replies = []
            for reply in comment.replies:
                comment_reply = self.get_reply_data(reply)
                replies.append(comment_reply)
            post_comment = self.get_comment_data(comment, replies)
            comments.append(post_comment)

        post = {"postid": get_post_dto.post.id, "posted_by": {"userid": get_post_dto.posted_by.user_id,
                                                              "username": get_post_dto.posted_by.username,
                                                              "profile_pic": get_post_dto.posted_by.profile_pic},
                "post_content": get_post_dto.post.post_content, "post_create_date": get_post_dto.post.post_create_date.strftime("%Y-%m-%d %H:%M:%S"),
                "reactions": {"count": get_post_dto.reactions.count,
                              "types": get_post_dto.reactions.types}, "comment_count": get_post_dto.comment_count,
                "comments": comments}

        return post

    def create_comment(self, comment_dto: CommentIdDTO):
        return {"comment_id": comment_dto.comment_id}

    def create_reply(self, reply_dto: CommentIdDTO):
        return {"reply_id": reply_dto.comment_id}

    def react_to_post_response(self, reaction_dto: ReactionIdDTO):
        return {"reaction_id": reaction_dto.reaction_id}

    def react_to_comment(self, reaction_dto: ReactionIdDTO):
        return {"reaction_id": reaction_dto.reaction_id}

    def get_comment_replies(self, replies_dto: List[RepliesDTO]):
        replies = []
        for reply_dto in replies_dto:
            reply = {"comment_id": reply_dto.comment_id, "commenter": {"user_id": reply_dto.user.user_id,
                                                                       "username": reply_dto.user.username,
                                                                       "profile_pic": reply_dto.user.profile_pic},
                     "comment_create_date": reply_dto.comment_create_date.strftime("%Y-%m-%d %H:%M:%S"), "comment_message": reply_dto.comment_content}
            replies.append(reply)
        return {"replies": replies}

    def get_user_posts(self, posts_dto: UserPosts):
        user_posts = [self.get_post(get_post_dto) for get_post_dto in posts_dto.posts]
        return {"posts": user_posts}

    def get_reactions_to_post(self, reactions_dto: List[ReactionDetailsDTO]):
        reactions = []
        for reaction_dto in reactions_dto:
            reaction = {"user_id": reaction_dto.user_id, "username": reaction_dto.username,
                        "profile_pic": reaction_dto.profile_pic, "reaction": reaction_dto.reaction}
            reactions.append(reaction)

        return {"reactions": reactions}

    def get_posts_reacted_by_user(self, posts_dto: List[PostIdDTO]):
        posts = []
        for post_dto in posts_dto:
            post = {"postid": post_dto.post_id}
            posts.append(post)

        return {"posts": posts}

    def get_posts_with_more_positive_reactions(self, posts_dto: List[PostIdDTO]):
        posts = []
        for post_dto in posts_dto:
            post = {"postid": post_dto.post_id}
            posts.append(post)

        return {"posts": posts}

    def get_reaction_metrics(self, reactions_dto: List[ReactionCountDTO]):
        reactions = []
        for reaction_dto in reactions_dto:
            reaction_metric = {"count": reaction_dto.count, "reaction": reaction_dto.reaction}
            reactions.append(reaction_metric)

        return {"reactions": reactions}

    def get_total_reaction_count(self, count_dto: TotalReactionDTO):
        return {"total_count": count_dto.count}

    def delete_post(self, post_id: PostIdDTO):
        return {"post_id": post_id.post_id}

    def post_not_exists(self):
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid post id', 'INVALID_POST_ID')

    def raise_not_comment(self):
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid comment id', 'INVALID_COMMENT_ID')
