from unittest.mock import Mock
import unittest

from fb_post_v2.interactors.get_posts_reacted_by_user_interactor import \
    GetPostsReactedByUserInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage


class TestGetPostsReactedByUser(unittest.TestCase):
    def test_posts_reacted_by_user(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_posts_reacted = GetPostsReactedByUserInteractor(post_storage_mock,
                                                            presenter_mock)

        user_id = 1
        posts_ids = [1, 2, 3]
        response_data = {"posts": [{"post_id": 1},
                                   {"post_id": 2}]}

        post_storage_mock.get_user_reacted_posts.return_value = posts_ids
        presenter_mock.get_user_reacted_posts_response.return_value = \
            response_data

        response = get_posts_reacted.get_posts_reacted_by_user(user_id)

        post_storage_mock.get_user_reacted_posts.assert_called_once_with(
            user_id)
        presenter_mock.get_user_reacted_posts_response.assert_called_once_with(
            posts_ids)
        assert response == response_data
