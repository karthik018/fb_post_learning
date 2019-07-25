from typing import List, Optional

from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import TotalReactionCountDTO, \
    ReactionCountDTO, UserReactionDTO, ReplyDTO, GetPostDTO, UserDTO, \
    ReactionStatsDTO, UserPostsDTO


class Presenter(JsonPresenter):

    def get_create_post_response(self, post_id: int) -> dict:
        return {"postid": post_id}

    @staticmethod
    def get_user_dict(user_dto: UserDTO) -> dict:
        return {"userid": user_dto.user_id,
                "username": user_dto.username,
                "profile_pic": user_dto.profile_pic}

    @staticmethod
    def get_datetime_string(datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_reaction_dict(reaction_stats_dto: ReactionStatsDTO) -> dict:
        return {"count": reaction_stats_dto.count,
                "types": reaction_stats_dto.types}

    def get_comment_reaction_stats(self, comment_id, comment_reactions, ):
        try:
            reaction_stats_dto = comment_reactions[comment_id]

        except KeyError:
            reaction_stats_dto = ReactionStatsDTO(count=0, types=[])

        reactions_dict = self.get_reaction_dict(reaction_stats_dto)

        return reactions_dict

    @staticmethod
    def get_users_wise_dict(all_user_list):
        all_users_dict = {}
        for user in all_user_list:
            user_dict = {"userid": user.user_id, "username": user.username,
                         "profile_pic": user.profile_pic}
            all_users_dict[user.user_id] = user_dict

        return all_users_dict

    def get_comment_details_dict(self, comment, all_users_dict):
        comment_dict = {
            "commentid": comment.id,
            "commenter": all_users_dict[comment.user_id],
            "comment_message": comment.comment_content,
            "comment_create_date":
                self.get_datetime_string(
                    comment.comment_create_date)
        }
        return comment_dict

    def get_post_details_dict(self, post_dto, all_users_dict):
        post_dict = {
            "postid": post_dto.id,
            "posted_by": all_users_dict[post_dto.user_id],
            "post_content": post_dto.post_content,
            "post_create_date": self.get_datetime_string(
                post_dto.post_create_date)
        }
        return post_dict

    def get_replies_list_for_comment(self, comment_id, get_post_dto,
                                     all_users_dict):
        replies_list = []
        for reply in get_post_dto.comments:
            if reply.commented_on_id == comment_id:
                reply_dict = self.get_comment_details_dict(reply,
                                                           all_users_dict)
                reply_dict["reactions"] = self.get_comment_reaction_stats(
                    reply.id, get_post_dto.comment_reactions)
                replies_list.append(reply_dict)

        return replies_list

    def get_comments_list_with_replies_for_post(
            self, get_post_dto, all_users_dict):

        comments_list = []
        for comment in get_post_dto.comments:
            if comment.commented_on_id is None:
                replies = self.get_replies_list_for_comment(
                    comment.id, get_post_dto, all_users_dict)
                replies_count = len(replies)

                comment_dict = self.get_comment_details_dict(comment,
                                                             all_users_dict)
                comment_dict["reactions"] = self.get_comment_reaction_stats(
                    comment.id, get_post_dto.comment_reactions)
                comment_dict["replies_count"] = replies_count
                comment_dict["replies"] = replies

                comments_list.append(comment_dict)

        return comments_list

    def get_post_response(self, get_post_dto: GetPostDTO):

        all_users_dict = self.get_users_wise_dict(get_post_dto.all_users)

        all_post_comments = self.get_comments_list_with_replies_for_post(
            get_post_dto, all_users_dict)

        comment_count = len(all_post_comments)

        post = self.get_post_details_dict(get_post_dto.post, all_users_dict)

        post["reactions"] = self.get_reaction_dict(
            get_post_dto.post_reactions)
        post["comments"] = all_post_comments
        post["comment_count"] = comment_count

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
            reply = {
                "comment_id": reply_dto.comment_id,
                "commenter": self.get_user_dict(reply_dto.user),
                "comment_create_date": self.get_datetime_string(
                    reply_dto.comment_create_date),
                "comment_message": reply_dto.comment_content
            }
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
