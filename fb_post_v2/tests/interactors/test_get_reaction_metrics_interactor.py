from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.get_reaction_metrics_interactor import GetReactionMetricsInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage, ReactionCountDTO


class TestReactionMetrics(unittest.TestCase):
    def test_reaction_metrics(self):
        reaction1_metrics_dto = Mock(spec=[field.name for field in fields(ReactionCountDTO)])
        reaction2_metrics_dto = Mock(spec=[field.name for field in fields(ReactionCountDTO)])
        reaction3_metrics_dto = Mock(spec=[field.name for field in fields(ReactionCountDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        reaction_metrics = GetReactionMetricsInteractor(post_storage_mock, presenter_mock)
        reactions_dto = [reaction1_metrics_dto, reaction2_metrics_dto, reaction3_metrics_dto]

        post_id = 1
        response_data = {"count": 1, "reaction": "LIKE"}

        post_storage_mock.get_reaction_metrics.return_value = reactions_dto
        presenter_mock.get_reaction_metrics.return_value = response_data
        response = reaction_metrics.get_reaction_metrics(post_id)

        post_storage_mock.get_reaction_metrics.assert_called_once_with(post_id)
        presenter_mock.get_reaction_metrics.assert_called_once_with(reactions_dto)
        assert response == response_data
