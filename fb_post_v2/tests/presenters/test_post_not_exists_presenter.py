from fb_post_v2.presenters.presenter import Presenter
import pytest


class TestPostNotExists:

    def test_post_not_exists(self):
        presenter = Presenter()

        from django_swagger_utils.drf_server.exceptions import BadRequest
        with pytest.raises(BadRequest):
            response = presenter.post_not_exists()

class TestDeletePost:

    def test_delete_post(self):
        presenter = Presenter()

        post_id =None

        response = presenter.get_delete_post_response(post_id)

        assert response["post_id"] == post_id



