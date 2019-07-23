from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage, PostIdDTO


class TestCreatePost(unittest.TestCase):
    def test_new_post(self):
        postid_dto = Mock(spec=[field.name for field in fields(PostIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_post = CreatePostInteractor(post_storage_mock, presenter_mock)

        post_storage_mock.create_post.return_value = postid_dto
        presenter_mock.get_create_post_response.return_value = {"post_id": 1}
        response = create_post.create_post("test post", 1)

        post_storage_mock.create_post.assert_called_once_with("test post", 1)
        presenter_mock.get_create_post_response.assert_called_once_with(postid_dto)
        assert response == {"post_id": 1}
