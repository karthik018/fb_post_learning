import abc
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

@dataclass
class UserDTO:
    user_id: int
    username: str
    profile_pic: str

@dataclass
class PostDTO:
    id: int
    post_content: str
    post_create_date: datetime

@dataclass
class ReplyDTO:
    comment_id: int
    user: UserDTO
    comment_content: str
    comment_create_date: datetime

@dataclass
class ReactionDTO:
    id: int
    react_on_id: int
    reacted_by: int
    reaction: str

@dataclass
class ReactionStatsDTO:
    count: int
    types: List[str]


@dataclass
class CommentDTO:
    id: int
    user: UserDTO
    comment_content: str
    comment_create_date: datetime
    comment_reactions: ReactionStatsDTO


@dataclass
class CommentWithRepliesDTO(CommentDTO):
    replies_count: int
    replies: List[CommentDTO]


@dataclass
class UserReactionDTO(UserDTO):
    reaction: str


@dataclass
class GetPostDTO:
    post: PostDTO
    posted_by: UserDTO
    reactions: ReactionStatsDTO
    comments: List[CommentWithRepliesDTO]
    comment_count: int


@dataclass
class UserPostsDTO:
    posts: List[GetPostDTO]


@dataclass
class ReactionCountDTO:
    count: int
    reaction: str

@dataclass
class TotalReactionCountDTO:
    count: int


class PostStorage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, post_content: str, created_by: int) -> int:
        pass

    @abc.abstractmethod
    def get_post(self, post_id: int) -> GetPostDTO:
        pass

    @abc.abstractmethod
    def create_comment(self, post_id: int, commenter: int,
                       comment_content: str) -> int:
        pass

    @abc.abstractmethod
    def create_reply(self, comment_id: int, commenter: int,
                     comment_content: str) -> int:
        pass

    @abc.abstractmethod
    def add_post_reaction(self, post_id: int, reacted_by: int,
                          reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def add_comment_reaction(self, comment_id: int, reacted_by: int,
                             reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def get_comment_replies(self, comment_id: int, offset: int,
                            limit: int) -> List[ReplyDTO]:
        pass

    @abc.abstractmethod
    def get_user_posts(self, user_id: int, offset: int,
                       limit: int) -> UserPostsDTO:
        pass

    @abc.abstractmethod
    def get_post_reactions(self, post_id: int, offset: int,
                           limit: int) -> List[UserReactionDTO]:
        pass

    @abc.abstractmethod
    def get_user_reacted_posts(self, user_id: int) -> List[int]:
        pass

    @abc.abstractmethod
    def get_positive_reaction_posts(self) -> List[int]:
        pass

    @abc.abstractmethod
    def get_reaction_metrics(self, post_id: int) -> List[ReactionCountDTO]:
        pass

    @abc.abstractmethod
    def get_total_reaction_count(self) -> TotalReactionCountDTO:
        pass

    @abc.abstractmethod
    def delete_post(self, post_id) -> Optional[int]:
        pass

    @abc.abstractmethod
    def post_exists(self, post_id) -> bool:
        pass

    @abc.abstractmethod
    def post_reaction_exists(self, post_id: int,
                             reacted_by: int) -> ReactionDTO:
        pass

    @abc.abstractmethod
    def delete_post_reaction(self, post_id: int,
                             reacted_by: int) -> Optional[int]:
        pass

    @abc.abstractmethod
    def update_post_reaction(self, post_id: int, reacted_by: int,
                             reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def comment_reaction_exists(self, comment_id: int,
                                reacted_by: int) -> ReactionDTO:
        pass

    @abc.abstractmethod
    def delete_comment_reaction(self, comment_id: int,
                                reacted_by: int) -> int:
        pass

    @abc.abstractmethod
    def update_comment_reaction(self, comment_id: int, reacted_by: int,
                                reaction_type: str) -> int:
        pass

    @abc.abstractmethod
    def is_comment_or_reply(self, comment_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_comment_id(self, reply_id: int) -> int:
        pass
