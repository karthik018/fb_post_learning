from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.get_posts_reacted_by_user_interactor import GetPostsReactedByUserInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage, UserPosts


class TestGetPostsReactedByUser(unittest.TestCase):
    def test_posts_reacted_by_user(self):
        userposts_dto = Mock(spec=[field.name for field in fields(UserPosts)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_posts_reacted = GetPostsReactedByUserInteractor(post_storage_mock, presenter_mock)

        user_id = 1
        response_data = [{"post_id": 1},
                         {"post_id": 2}]

        post_storage_mock.get_posts_reacted_by_user.return_value = userposts_dto
        presenter_mock.get_posts_reacted_by_user.return_value = response_data
        response = get_posts_reacted.get_posts_reacted_by_user(user_id)

        post_storage_mock.get_posts_reacted_by_user.assert_called_once_with(user_id)
        presenter_mock.get_posts_reacted_by_user.assert_called_once_with(userposts_dto)
        assert response == response_data
