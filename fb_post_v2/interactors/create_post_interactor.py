from fb_post_v2.interactors.storages.post_storage import PostStorage
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter

class CreatePostInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def create_post(self, post_content: str, created_by: int) -> dict:
        post_dto = self.post_storage.create_post(post_content, created_by)
        response = self.presenter.get_create_post_response(post_dto)
        return response
