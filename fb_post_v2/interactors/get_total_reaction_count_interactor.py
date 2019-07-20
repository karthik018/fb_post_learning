from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage

class GetTotalReactionCountInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def get_total_reaction_count(self) -> dict:
        count_dto = self.post_storage.get_total_reaction_count()
        response = self.presenter.get_total_reaction_count(count_dto)
        return response
