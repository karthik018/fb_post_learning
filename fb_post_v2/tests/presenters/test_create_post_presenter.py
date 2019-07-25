
from fb_post_v2.presenters.presenter import JsonPresenter

class TestCreatePost:

    def test_create_post(self):
        presenter = JsonPresenter()
        post_id = 1

        response = presenter.get_create_post_response(post_id)

        assert response["postid"] == post_id
