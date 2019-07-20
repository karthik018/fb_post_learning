from unittest.mock import Mock
import unittest
from dataclasses import fields

from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.replies_for_comment_interactor import CommentRepliesInteractor
from fb_post_v2.interactors.storages.post_storage import CommentDTO, PostStorage
from django.core.exceptions import SuspiciousOperation


class TestCommentReplies(unittest.TestCase):
    def test_comment_replies(self):
        reply1_dto = Mock(spec=[field.name for field in fields(CommentDTO)])
        reply2_dto = Mock(spec=[field.name for field in fields(CommentDTO)])
        reply3_dto = Mock(spec=[field.name for field in fields(CommentDTO)])
        replies_dto = [reply1_dto, reply2_dto, reply3_dto]
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_comment_replies = CommentRepliesInteractor(post_storage_mock, presenter_mock)

        comment_id = 1
        response_data = {"replies": [{"reply": 2}, {"reply": 4}]}

        post_storage_mock.check_comment_or_reply.return_value = True
        post_storage_mock.get_comment_replies.return_value = replies_dto
        presenter_mock.get_comment_replies.return_value = response_data
        response = get_comment_replies.get_comment_replies(comment_id)

        post_storage_mock.check_comment_or_reply.assert_called_once_with(comment_id)
        post_storage_mock.get_comment_replies.assert_called_once_with(comment_id)
        presenter_mock.get_comment_replies.assert_called_once_with(replies_dto)
        assert response == response_data

    def test_not_comment(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        get_comment_replies = CommentRepliesInteractor(post_storage_mock, presenter_mock)

        comment_id = 2

        post_storage_mock.check_comment_or_reply.return_value = False
        presenter_mock.raise_not_comment.side_effect = SuspiciousOperation
        with self.assertRaises(SuspiciousOperation):
            response = get_comment_replies.get_comment_replies(comment_id)

        post_storage_mock.check_comment_or_reply.assert_called_once_with(comment_id)
        presenter_mock.raise_not_comment.assert_called_once()
