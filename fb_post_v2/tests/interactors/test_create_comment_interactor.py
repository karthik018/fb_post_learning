from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.create_comment_interactor import CreateCommentInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage, CommentDTO, CommentIdDTO


class TestReplyToComment(unittest.TestCase):
    def test_reply_to_reply(self):
        comment_dto = Mock(spec=[field.name for field in fields(CommentDTO)])
        comment_id_dto = Mock(spec=[field.name for field in fields(CommentIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock, presenter_mock)

        comment_id = 2
        commenter = 1
        comment_content = "test comment"
        response_data = {"comment_id": 3}
        comment_id_dto.comment_id = 1

        post_storage_mock.check_comment_or_reply.return_value = False
        post_storage_mock.get_comment_id.return_value = comment_id_dto
        post_storage_mock.create_reply.return_value = comment_id_dto
        presenter_mock.create_reply.return_value = response_data
        response = create_comment.create_reply(comment_id, commenter, comment_content)

        post_storage_mock.get_comment_id.assert_called_once_with(comment_id)
        post_storage_mock.create_reply.assert_called_once_with(comment_id_dto.comment_id, commenter, comment_content)
        presenter_mock.create_reply.assert_called_once_with(comment_id_dto)
        assert response == response_data

    def test_reply_to_comment(self):
        comment_id_dto = Mock(spec=[field.name for field in fields(CommentIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock, presenter_mock)

        comment_id = 1
        commenter = 1
        comment_content = "test comment"
        response_data = {"comment_id": 2}

        post_storage_mock.check_comment_or_reply.return_value = True
        post_storage_mock.create_reply.return_value = comment_id_dto
        presenter_mock.create_reply.return_value = response_data
        response = create_comment.create_reply(comment_id, commenter, comment_content)

        post_storage_mock.create_reply.assert_called_once_with(comment_id, commenter, comment_content)
        presenter_mock.create_reply.assert_called_once_with(comment_id_dto)
        assert response == response_data

class TestCreateComment(unittest.TestCase):
    def test_create_comment(self):
        comment_id_dto = Mock(spec=[field.name for field in fields(CommentIdDTO)])
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock, presenter_mock)

        post_id = 1
        commenter = 1
        comment_content = "test comment"
        response_data = {"comment_id": 1}

        post_storage_mock.create_comment.return_value = comment_id_dto
        presenter_mock.create_comment.return_value = response_data
        response = create_comment.create_comment(post_id, commenter, comment_content)

        post_storage_mock.create_comment.assert_called_once_with(post_id, commenter, comment_content)
        presenter_mock.create_comment.assert_called_once_with(comment_id_dto)
        assert response == response_data
