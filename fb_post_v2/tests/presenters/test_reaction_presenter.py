from fb_post_v2.presenters.presenter import Presenter

class TestReactToPost:

    def test_react_to_post_response(self):
        presenter = Presenter()

        reaction_id = 1

        response = presenter.get_add_post_reaction_response(reaction_id)

        assert response["reactionid"] == reaction_id


class TestReactToComment:

    def test_react_to_comment(self):
        presenter = Presenter()

        reaction_id = 2

        response = presenter.get_add_comment_reaction_response(reaction_id)

        assert response["reactionid"] == reaction_id
