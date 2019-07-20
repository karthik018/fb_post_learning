from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage


class CommentRepliesInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def get_comment_replies(self, comment_id: int) -> dict:
        comment = self.post_storage.check_comment_or_reply(comment_id)
        if comment:
            replies_dto = self.post_storage.get_comment_replies(comment_id)
            response = self.presenter.get_comment_replies(replies_dto)
            return response
        self.presenter.raise_not_comment()
