from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage


class ReactInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def react_to_post(self, post_id: int, reacted_by: int, reaction_type: str) -> dict:
        try:
            reaction_dto = self.post_storage.post_reaction_exists(post_id, reacted_by)
            if reaction_dto.reaction == reaction_type:
                delete_reaction = self.post_storage.delete_post_reaction(post_id, reacted_by)
                response = self.presenter.get_react_to_post_response(delete_reaction)
            else:
                update_reaction = self.post_storage.update_post_reaction(post_id, reacted_by, reaction_type)
                response = self.presenter.get_react_to_post_response(update_reaction)
        except:
            reaction_dto = self.post_storage.react_to_post(post_id, reacted_by, reaction_type)
            response = self.presenter.get_react_to_post_response(reaction_dto)

        return response

    def react_to_comment(self, comment_id: int, reacted_by: int, reaction_type: str) -> dict:
        try:
            reaction_dto = self.post_storage.comment_reaction_exists(comment_id, reacted_by)
            if reaction_dto.reaction == reaction_type:
                delete_reaction = self.post_storage.delete_comment_reaction(comment_id, reacted_by)
                response = self.presenter.get_react_to_comment_response(delete_reaction)
            else:
                update_reaction = self.post_storage.update_comment_reaction(comment_id, reacted_by, reaction_type)
                response = self.presenter.get_react_to_comment_response(update_reaction)
        except:
            reaction_dto = self.post_storage.react_to_comment(comment_id, reacted_by, reaction_type)
            response = self.presenter.get_react_to_comment_response(reaction_dto)

        return response
