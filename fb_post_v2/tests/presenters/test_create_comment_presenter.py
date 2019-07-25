from fb_post_v2.presenters.presenter import Presenter
class TestCreateComment:

    def test_create_comment(self):
        presenter = Presenter()

        comment_id = 1

        response = presenter.get_create_comment_response(comment_id)

        assert response["comment_id"] == comment_id
