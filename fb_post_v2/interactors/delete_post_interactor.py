from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage

class DeletePostInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def delete_post(self, post_id: int) -> dict:
        post_exists = self.post_storage.post_exists(post_id)
        if post_exists:
            post_dto = self.post_storage.delete_post(post_id)
            response = self.presenter.get_delete_post_response(post_dto)
            return response
        return self.presenter.post_not_exists()
