from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.get_user_posts_interactor import GetUserPostsInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import UserPosts, PostStorage


class TestUserPosts(unittest.TestCase):
    def test_user_posts(self):
        user_posts_dto = Mock(spec=[field.name for field in fields(UserPosts)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_user_posts = GetUserPostsInteractor(post_storage_mock, presenter_mock)

        user_id = 1
        offset = 0
        limit = 1
        response_data = {"posts": [{"post_id": 1}, {"post_id": 5}]}

        post_storage_mock.get_user_posts.return_value = user_posts_dto
        presenter_mock.get_user_posts_response.return_value = response_data
        response = get_user_posts.get_user_posts(user_id, offset, limit)

        post_storage_mock.get_user_posts.assert_called_once_with(user_id, offset, limit)
        presenter_mock.get_user_posts_response.assert_called_once_with(user_posts_dto)
        assert response == response_data
