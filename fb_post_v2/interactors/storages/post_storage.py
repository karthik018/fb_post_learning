import abc
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict


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
class PostIdDTO:
    post_id: int

@dataclass
class RepliesDTO:
    comment_id: int
    user: UserDTO
    comment_content: str
    comment_create_date: datetime

@dataclass
class CommentIdDTO:
    comment_id: int

@dataclass
class ReactionDTO:
    id: int
    react_on_id: int
    reacted_by: int
    reaction: str

@dataclass
class ReactionIdDTO:
    reaction_id: int

@dataclass
class ReactionsDTO:
    count: int
    types: List[str]

@dataclass
class CommentDTO:
    id: int
    user: UserDTO
    comment_content: str
    comment_create_date: datetime
    comment_reactions: ReactionsDTO

@dataclass
class CommentWithRepliesDTO(CommentDTO):
    replies_count: int
    replies: List[CommentDTO]

@dataclass
class ReactionDetailsDTO(UserDTO):
    reaction: str

@dataclass
class GetPostDTO:
    post: PostDTO
    posted_by: UserDTO
    reactions: ReactionsDTO
    comments: List[CommentWithRepliesDTO]
    comment_count: int

@dataclass
class UserPosts:
    posts: List[GetPostDTO]

@dataclass
class ReactionCountDTO:
    count: int
    reaction: str

@dataclass
class TotalReactionDTO:
    count: int

class PostStorage:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, post_content: str, created_by: int) -> PostIdDTO:
        pass

    @abc.abstractmethod
    def get_post(self, post_id: int) -> GetPostDTO:
        pass

    @abc.abstractmethod
    def create_comment(self, post_id: int, commenter: int, comment_content: str) -> CommentIdDTO:
        pass

    @abc.abstractmethod
    def create_reply(self, comment_id: int, commenter: int, comment_content: str) -> CommentIdDTO:
        pass

    @abc.abstractmethod
    def react_to_post(self, post_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        pass

    @abc.abstractmethod
    def react_to_comment(self, comment_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        pass

    @abc.abstractmethod
    def get_comment_replies(self, comment_id: int, offset: int, limit: int) -> List[RepliesDTO]:
        pass

    @abc.abstractmethod
    def get_user_posts(self, user_id: int, offset: int, limit: int) -> UserPosts:
        pass

    @abc.abstractmethod
    def get_reactions_to_post(self, post_id: int, offset: int, limit: int) -> List[ReactionDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_posts_reacted_by_user(self, user_id: int) -> List[PostIdDTO]:
        pass

    @abc.abstractmethod
    def get_posts_with_more_positive_reactions(self) -> List[PostIdDTO]:
        pass

    @abc.abstractmethod
    def get_reaction_metrics(self, post_id: int) -> List[ReactionCountDTO]:
        pass

    @abc.abstractmethod
    def get_total_reaction_count(self) -> TotalReactionDTO:
        pass

    @abc.abstractmethod
    def delete_post(self, post_id) -> PostIdDTO:
        pass

    @abc.abstractmethod
    def post_exists(self, post_id) -> bool:
        pass

    @abc.abstractmethod
    def post_reaction_exists(self, post_id: int, reacted_by: int) -> ReactionDTO:
        pass

    @abc.abstractmethod
    def delete_post_reaction(self, post_id: int, reacted_by: int) -> ReactionIdDTO:
        pass

    @abc.abstractmethod
    def update_post_reaction(self, post_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        pass

    @abc.abstractmethod
    def comment_reaction_exists(self, comment_id: int, reacted_by: int) -> ReactionDTO:
        pass

    @abc.abstractmethod
    def delete_comment_reaction(self, comment_id: int, reacted_by: int) -> ReactionIdDTO:
        pass

    @abc.abstractmethod
    def update_comment_reaction(self, comment_id: int, reacted_by: int, reaction_type: str) -> ReactionIdDTO:
        pass

    @abc.abstractmethod
    def check_comment_or_reply(self, comment_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_comment_id(self, comment_id: int) -> CommentIdDTO:
        pass
