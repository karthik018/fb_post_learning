import abc

from typing import List, Optional

from fb_post_v2.interactors.storages.post_storage import GetPostDTO, \
    UserReactionDTO, TotalReactionCountDTO, ReactionCountDTO, UserPostsDTO, \
    ReplyDTO


class JsonPresenter:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_create_post_response(self, post_id: int):
        pass

    @abc.abstractmethod
    def get_post_response(self, get_post_dto: GetPostDTO):
        pass

    @abc.abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass

    @abc.abstractmethod
    def get_create_reply_response(self, reply_id: int):
        pass

    @abc.abstractmethod
    def get_add_post_reaction_response(self, reaction_id: int):
        pass

    @abc.abstractmethod
    def get_add_comment_reaction_response(self, reaction_id: int):
        pass

    @abc.abstractmethod
    def get_comment_replies_response(self, replies_dto: List[ReplyDTO]):
        pass

    @abc.abstractmethod
    def get_user_posts_response(self, posts_dto: UserPostsDTO):
        pass

    @abc.abstractmethod
    def get_post_reactions_response(self, reactions_dto: List[UserReactionDTO]):
        pass

    @abc.abstractmethod
    def get_user_reacted_posts_response(self, posts_dto: List[int]):
        pass

    @abc.abstractmethod
    def get_positive_reaction_posts_response(self, posts_dto: List[int]):
        pass

    @abc.abstractmethod
    def get_reaction_metrics_response(self, reactions_dto: List[ReactionCountDTO]):
        pass

    @abc.abstractmethod
    def get_total_reaction_count_response(self, count_dto: TotalReactionCountDTO):
        pass

    @abc.abstractmethod
    def get_delete_post_response(self, post_id: Optional[int]):
        pass

    @abc.abstractmethod
    def post_not_exists(self):
        pass

    @abc.abstractmethod
    def raise_not_comment(self):
        pass
