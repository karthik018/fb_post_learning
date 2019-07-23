from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.get_total_reaction_count_interactor import GetTotalReactionCountInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import TotalReactionDTO, PostStorage


class TestTotalReactionCount(unittest.TestCase):
    def test_total_reaction_count(self):
        total_count_dto = Mock(spec=[field.name for field in fields(TotalReactionDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        total_count = GetTotalReactionCountInteractor(post_storage_mock, presenter_mock)

        response_data = {"total_count": 5}

        post_storage_mock.get_total_reaction_count.return_value = total_count_dto
        presenter_mock.get_total_reaction_count_response.return_value = response_data
        response = total_count.get_total_reaction_count()

        post_storage_mock.get_total_reaction_count.assert_called_once()
        presenter_mock.get_total_reaction_count_response.assert_called_once_with(total_count_dto)
        assert response == response_data
