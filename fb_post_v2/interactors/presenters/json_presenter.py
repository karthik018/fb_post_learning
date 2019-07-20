import abc

from typing import List, Dict

from fb_post_v2.interactors.storages.post_storage import PostDTO, GetPostDTO, CommentDTO, ReactionDTO, \
    UserPosts, ReactionDetailsDTO, ReactionMetricsDTO, TotalReactionDTO, PostIdDTO, ReactionIdDTO, CommentIdDTO


class JsonPresenter:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, post_dto: PostIdDTO):
        pass

    @abc.abstractmethod
    def get_post(self, get_post_dto: GetPostDTO):
        pass

    @abc.abstractmethod
    def create_comment(self, comment_dto: CommentIdDTO):
        pass

    @abc.abstractmethod
    def create_reply(self, reply_dto: CommentIdDTO):
        pass

    @abc.abstractmethod
    def react_to_post_response(self, reaction_dto: ReactionIdDTO):
        pass

    @abc.abstractmethod
    def react_to_comment(self, reaction_dto: ReactionIdDTO):
        pass

    @abc.abstractmethod
    def get_comment_replies(self, replies_dto: List[CommentDTO]):
        pass

    @abc.abstractmethod
    def get_user_posts(self, posts_dto: UserPosts):
        pass

    @abc.abstractmethod
    def get_reactions_to_post(self, reactions_dto: List[ReactionDetailsDTO]):
        pass

    @abc.abstractmethod
    def get_posts_reacted_by_user(self, posts_dto: UserPosts):
        pass

    @abc.abstractmethod
    def get_posts_with_more_positive_reactions(self, posts_dto: List[PostIdDTO]):
        pass

    @abc.abstractmethod
    def get_reaction_metrics(self, reactions_dto: List[ReactionMetricsDTO]):
        pass

    @abc.abstractmethod
    def get_total_reaction_count(self, count_dto: TotalReactionDTO):
        pass

    @abc.abstractmethod
    def delete_post(self, post_id: Dict):
        pass

    @abc.abstractmethod
    def post_not_exists(self):
        pass

    @abc.abstractmethod
    def delete_post_reaction(self):
        pass

    @abc.abstractmethod
    def raise_not_comment(self):
        pass