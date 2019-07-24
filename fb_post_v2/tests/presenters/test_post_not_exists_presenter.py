from fb_post_v2.interactors.storages.post_storage import PostIdDTO
from fb_post_v2.presenters.presenter import JsonPresenter
import pytest


class TestPostNotExists:

    def test_post_not_exists(self):
        presenter = JsonPresenter()

        from django_swagger_utils.drf_server.exceptions import BadRequest
        with pytest.raises(BadRequest):
            response = presenter.post_not_exists()

class TestDeletePost:

    def test_delete_post(self):
        presenter = JsonPresenter()

        post_id_dto = PostIdDTO(post_id=None)

        response = presenter.get_delete_post_response(post_id_dto)

        assert response["post_id"] == post_id_dto.post_id



