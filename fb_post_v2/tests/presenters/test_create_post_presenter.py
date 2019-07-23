import pytest
from freezegun import freeze_time

from fb_post_v2.interactors.storages.post_storage import PostIdDTO
from fb_post_v2.presenters.presenter import JsonPresenter

class TestCreatePost:

    def test_create_post(self):
        presenter = JsonPresenter()
        post_dto = PostIdDTO(post_id=1)

        response = presenter.create_post(post_dto=post_dto)

        assert response["post_id"] == post_dto.post_id
