from unittest.mock import Mock
import unittest
from dataclasses import fields
from fb_post_v2.interactors.react_interactor import ReactInteractor
from fb_post_v2.interactors.storages.post_storage import PostStorage, ReactionDTO, ReactionIdDTO
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from django.core.exceptions import ObjectDoesNotExist

class TestPostReaction(unittest.TestCase):
    def test_new_reaction(self):
        reaction_id_dto = Mock(spec=[field.name for field in fields(ReactionIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)

        reaction_interactor = ReactInteractor(post_storage_mock, presenter_mock)
        post_storage_mock.post_reaction_exists.side_effect = ObjectDoesNotExist
        post_storage_mock.react_to_post.return_value = reaction_id_dto
        presenter_mock.react_to_post_response.return_value = {"reaction_id": 1}
        response = reaction_interactor.react_to_post(1, 1, "LIKE")

        post_storage_mock.react_to_post.assert_called_once_with(1, 1, "LIKE")
        presenter_mock.react_to_post_response.assert_called_once_with(reaction_id_dto)
        assert response == {"reaction_id": 1}

    def test_same_reaction(self):
        reaction_dto = Mock(spec=[field.name for field in fields(ReactionDTO)])
        reaction_id_dto = Mock(spec=[field.name for field in fields(ReactionIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)

        reaction_interactor = ReactInteractor(post_storage_mock, presenter_mock)
        post_storage_mock.post_reaction_exists.return_value = reaction_dto
        reaction_dto.reaction = "LIKE"
        post_storage_mock.delete_post_reaction.return_value = reaction_id_dto
        presenter_mock.react_to_post_response.return_value = {"reaction_id": None}
        response = reaction_interactor.react_to_post(1, 1, "LIKE")

        post_storage_mock.delete_post_reaction.assert_called_once_with(1, 1)
        presenter_mock.react_to_post_response.assert_called_once_with(reaction_id_dto)
        assert response == {"reaction_id": None}

    def test_different_reaction(self):
        reaction_dto = Mock(spec=[field.name for field in fields(ReactionDTO)])
        reaction_id_dto = Mock(spec=[field.name for field in fields(ReactionIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)

        reaction_interactor = ReactInteractor(post_storage_mock, presenter_mock)
        post_storage_mock.post_reaction_exists.return_value = reaction_dto
        reaction_dto.reaction = "LOVE"
        post_storage_mock.update_post_reaction.return_value = reaction_id_dto
        presenter_mock.react_to_post_response.return_value = {"reaction_id": 1}
        response = reaction_interactor.react_to_post(1, 1, "LIKE")

        post_storage_mock.update_post_reaction.assert_called_once_with(1, 1, "LIKE")
        presenter_mock.react_to_post_response.assert_called_once_with(reaction_id_dto)
        assert response == {"reaction_id": 1}


class TestCommentReaction(unittest.TestCase):
    def test_new_reaction(self):
        reaction_id_dto = Mock(spec=[field.name for field in fields(ReactionIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)

        reaction_interactor = ReactInteractor(post_storage_mock, presenter_mock)
        post_storage_mock.comment_reaction_exists.side_effect = ObjectDoesNotExist
        post_storage_mock.react_to_comment.return_value = reaction_id_dto
        presenter_mock.react_to_comment.return_value = {"reaction_id": 1}
        response = reaction_interactor.react_to_comment(1, 1, "LIKE")

        post_storage_mock.react_to_comment.assert_called_once_with(1, 1, "LIKE")
        presenter_mock.react_to_comment.assert_called_once_with(reaction_id_dto)
        assert response == {"reaction_id": 1}

    def test_same_reaction(self):
        reaction_dto = Mock(spec=[field.name for field in fields(ReactionDTO)])
        reaction_id_dto = Mock(spec=[field.name for field in fields(ReactionIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        reaction_interactor = ReactInteractor(post_storage_mock, presenter_mock)

        post_storage_mock.comment_reaction_exists.return_value = reaction_dto
        reaction_dto.reaction = "LIKE"
        post_storage_mock.delete_comment_reaction.return_value = reaction_id_dto
        presenter_mock.react_to_comment.return_value = {"reaction_id": None}
        response = reaction_interactor.react_to_comment(1, 1, "LIKE")

        post_storage_mock.delete_comment_reaction.assert_called_once_with(1, 1)
        presenter_mock.react_to_comment.assert_called_once_with(reaction_id_dto)
        assert response == {"reaction_id": None}

    def test_different_reaction(self):
        reaction_dto = Mock(spec=[field.name for field in fields(ReactionDTO)])
        reaction_id_dto = Mock(spec=[field.name for field in fields(ReactionIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)

        reaction_interactor = ReactInteractor(post_storage_mock, presenter_mock)
        post_storage_mock.comment_reaction_exists.return_value = reaction_dto
        reaction_dto.reaction = "LOVE"
        post_storage_mock.update_comment_reaction.return_value = reaction_id_dto
        presenter_mock.react_to_comment.return_value = {"reaction_id": 1}
        response = reaction_interactor.react_to_comment(1, 1, "LIKE")

        post_storage_mock.update_comment_reaction.assert_called_once_with(1, 1, "LIKE")
        presenter_mock.react_to_comment.assert_called_once_with(reaction_id_dto)
        assert response == {"reaction_id": 1}

