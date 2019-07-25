from unittest.mock import Mock
import unittest

from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage


class TestCreatePost(unittest.TestCase):
    def test_new_post(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_post = CreatePostInteractor(post_storage_mock, presenter_mock)

        post_id = 1

        post_storage_mock.create_post.return_value = post_id
        presenter_mock.get_create_post_response.return_value = {"post_id": 1}
        response = create_post.create_post("test post", 1)

        post_storage_mock.create_post.assert_called_once_with("test post", 1)
        presenter_mock.get_create_post_response.assert_called_once_with(post_id)
        assert response == {"post_id": 1}
