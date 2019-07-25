
from fb_post_v2.presenters.presenter import Presenter

class TestCreatePost:

    def test_create_post(self):
        presenter = Presenter()
        post_id = 1

        response = presenter.get_create_post_response(post_id)

        assert response["postid"] == post_id
