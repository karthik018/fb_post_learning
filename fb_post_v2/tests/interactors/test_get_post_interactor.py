from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.get_post_interactor import GetPostInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage, GetPostDTO


class TestGetPost(unittest.TestCase):
    def test_get_post(self):
        getpost_dto = Mock(spec=[field.name for field in fields(GetPostDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_post = GetPostInteractor(post_storage_mock, presenter_mock)

        post_id = 1
        response_data = {"post_id": 1}

        post_storage_mock.get_post.return_value = getpost_dto
        presenter_mock.get_post.return_value = response_data
        response = get_post.get_post(post_id)

        post_storage_mock.get_post.assert_called_once_with(post_id)
        presenter_mock.get_post.assert_called_once_with(getpost_dto)
        assert response == response_data
