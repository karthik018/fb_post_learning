from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.get_reactions_to_post_interactor \
    import GetReactionsToPostInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import UserReactionDTO, \
    PostStorage


class TestPostReactions(unittest.TestCase):

    def test_post_reactions(self):

        reaction1_dto = Mock(
            spec=[field.name for field in fields(UserReactionDTO)])

        reaction2_dto = Mock(
            spec=[field.name for field in fields(UserReactionDTO)])

        reaction3_dto = Mock(
            spec=[field.name for field in fields(UserReactionDTO)])

        reactions_dto = [reaction1_dto, reaction2_dto, reaction3_dto]
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_reactions_to_post = GetReactionsToPostInteractor(post_storage_mock,
                                                             presenter_mock)

        post_id = 1
        offset = 0
        limit = 1
        response_data = {
            "reactions": [{"reaction": "LIKE"}, {"reaction": "LOVE"}]}

        post_storage_mock.get_post_reactions.return_value = reactions_dto
        presenter_mock.get_post_reactions_response.return_value = response_data
        response = get_reactions_to_post.get_reactions_to_post(post_id, offset,
                                                               limit)

        post_storage_mock.get_post_reactions.assert_called_once_with(
            post_id, offset, limit)
        presenter_mock.get_post_reactions_response.assert_called_once_with(
            reactions_dto)

        assert response == response_data
