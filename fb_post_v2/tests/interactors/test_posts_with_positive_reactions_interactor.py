from dataclasses import fields
from unittest.mock import Mock
import unittest

from fb_post_v2.interactors.get_posts_with_more_positive_reactions_interactor import \
    GetPostsWithPositiveReactionsInteractor
from fb_post_v2.interactors.storages.post_storage import PostStorage, PostDTO, PostIdDTO
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter

class TestPostsWithPositiveReactions(unittest.TestCase):
    def test_posts_with_positive_reactions(self):
        post1_dto = Mock(spec=[field.name for field in fields(PostIdDTO)])
        post2_dto = Mock(spec=[field.name for field in fields(PostIdDTO)])
        post3_dto = Mock(spec=[field.name for field in fields(PostIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_posts_with_more_positive_reactions = GetPostsWithPositiveReactionsInteractor(post_storage_mock,
                                                                                         presenter_mock)

        response_data = {"posts": [{"post_id": 1},
                         {"post_id": 2},
                         {"post_id": 3}]}

        post_storage_mock.get_posts_with_more_positive_reactions.return_value = [post1_dto, post2_dto,
                                                                                 post3_dto]
        presenter_mock.get_posts_with_more_positive_reactions.return_value = response_data
        response = get_posts_with_more_positive_reactions.get_posts_with_more_positive_reactions()

        post_storage_mock.get_posts_with_more_positive_reactions.assert_called_once()
        presenter_mock.get_posts_with_more_positive_reactions.assert_called_once()
        assert response == response_data

