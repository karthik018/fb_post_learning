from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage


class ReactToPostInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def react_to_post(self, post_id: int, reacted_by: int, reaction_type: str) -> dict:
        try:
            reaction_dto = self.post_storage.post_reaction_exists(post_id, reacted_by)
            if reaction_dto.reaction == reaction_type:
                delete_reaction = self.post_storage.delete_post_reaction(post_id, reacted_by)
                return self.presenter.react_to_post(delete_reaction)
            else:
                update_reaction = self.post_storage.update_post_reaction(post_id, reacted_by, reaction_type)
                return self.presenter.react_to_post(update_reaction)
        except:
            reaction_dto = self.post_storage.react_to_post(post_id, reacted_by, reaction_type)
            response = self.presenter.react_to_post(reaction_dto)
            return response
