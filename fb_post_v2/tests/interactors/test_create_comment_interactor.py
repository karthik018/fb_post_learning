from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.create_comment_interactor import CreateCommentInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage, CommentDTO, CommentIdDTO


class TestReplyToComment(unittest.TestCase):
    def test_comment_or_reply(self):
        comment_dto = Mock(spec=[field.name for field in fields(CommentDTO)])
        comment_id_dto = Mock(spec=[field.name for field in fields(CommentIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock, presenter_mock)

        post_storage_mock.check_comment_or_reply.return_value = False
        comment_dto.id = 1
        post_storage_mock.get_comment.return_value = comment_dto
        post_storage_mock.create_reply.return_value = comment_id_dto
        presenter_mock.create_reply.return_value = {"comment_id": 3}
        response = create_comment.create_reply(2, 1, "comment")

        post_storage_mock.get_comment.assert_called_once_with(2)
        post_storage_mock.create_reply.assert_called_once_with(1, 1, "comment")
        presenter_mock.create_reply.assert_called_once_with(comment_id_dto)
        assert response == {"comment_id": 3}

    def test_comment_reply(self):
        comment_id_dto = Mock(spec=[field.name for field in fields(CommentIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock, presenter_mock)

        post_storage_mock.check_comment_or_reply.return_value = True
        post_storage_mock.create_reply.return_value = comment_id_dto
        presenter_mock.create_reply.return_value = {"comment_id": 2}
        response = create_comment.create_reply(1, 1, "comment")

        post_storage_mock.create_reply.assert_called_once_with(1, 1, "comment")
        presenter_mock.create_reply.assert_called_once_with(comment_id_dto)
        assert response == {"comment_id": 2}

class TestCreateComment(unittest.TestCase):
    def test_create_comment(self):
        comment_id_dto = Mock(spec=[field.name for field in fields(CommentIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock, presenter_mock)

        post_storage_mock.create_comment.return_value = comment_id_dto
        presenter_mock.create_comment.return_value = {"comment_id": 1}
        response = create_comment.create_comment(1, 1, "comment")

        post_storage_mock.create_comment.assert_called_once_with(1, 1, "comment")
        presenter_mock.create_comment.assert_called_once_with(comment_id_dto)
        assert response == {"comment_id": 1}
