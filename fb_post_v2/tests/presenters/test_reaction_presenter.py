from fb_post_v2.interactors.storages.post_storage import ReactionIdDTO
from fb_post_v2.presenters.presenter import JsonPresenter

class TestReactToPost:

    def test_react_to_post_response(self):
        presenter = JsonPresenter()

        reaction_dto = ReactionIdDTO(reaction_id=1)

        response = presenter.get_react_to_post_response(reaction_dto)

        assert response["reactionid"] == reaction_dto.reaction_id


class TestReactToComment:

    def test_react_to_comment(self):
        presenter = JsonPresenter()

        reaction_dto = ReactionIdDTO(reaction_id=2)

        response = presenter.get_react_to_comment_response(reaction_dto)

        assert response["reactionid"] == reaction_dto.reaction_id
