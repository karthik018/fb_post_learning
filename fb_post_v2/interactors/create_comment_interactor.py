from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage


class CreateCommentInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def create_comment(self, post_id: int, commenter: int, comment_content: str) -> dict:
        comment_dto = self.post_storage.create_comment(post_id, commenter, comment_content)
        response = self.presenter.create_comment(comment_dto)
        return response

    def create_reply(self, comment_id: int, commenter: int, comment_content: str) -> dict:
        comment = self.post_storage.check_comment_or_reply(comment_id)
        if not comment:
            comment_dto = self.post_storage.get_comment(comment_id)
            comment_id = comment_dto.id
        reply_dto = self.post_storage.create_reply(comment_id, commenter, comment_content)
        response = self.presenter.create_reply(reply_dto)
        return response
