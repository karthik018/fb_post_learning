from dataclasses import fields
from unittest.mock import Mock
import unittest

from fb_post_v2.interactors.get_posts_with_more_positive_reactions_interactor import \
    GetPostsWithPositiveReactionsInteractor
from fb_post_v2.interactors.storages.post_storage import PostStorage, PostDTO
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter


class TestPostsWithPositiveReactions(unittest.TestCase):
    def test_posts_with_positive_reactions(self):
        post1_id = 1
        post2_id = 2
        post3_id = 3
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        positive_reaction_posts = GetPostsWithPositiveReactionsInteractor(
            post_storage_mock,
            presenter_mock)

        response_data = {"posts": [{"post_id": 1},
                                   {"post_id": 2},
                                   {"post_id": 3}]}

        post_storage_mock.get_positive_reaction_posts.return_value = [post1_id,
                                                                      post2_id,
                                                                      post3_id]

        presenter_mock.get_positive_reaction_posts_response.return_value = \
            response_data

        response = positive_reaction_posts \
            .get_posts_with_more_positive_reactions()

        post_storage_mock.get_positive_reaction_posts.assert_called_once()
        presenter_mock.get_positive_reaction_posts_response.assert_called_once()
        assert response == response_data
