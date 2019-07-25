from unittest.mock import Mock
import unittest

from fb_post_v2.interactors.create_comment_interactor import \
    CreateCommentInteractor
from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage


class TestReplyToComment(unittest.TestCase):
    def test_reply_to_reply(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock,
                                                 presenter_mock)

        reply_id = 2
        commenter = 1
        comment_content = "test comment"
        response_data = {"comment_id": 3}
        comment_id = 1

        post_storage_mock.is_comment_or_reply.return_value = False
        post_storage_mock.get_comment_id.return_value = comment_id
        post_storage_mock.create_reply.return_value = comment_id
        presenter_mock.get_create_reply_response.return_value = response_data
        response = create_comment.create_reply(reply_id, commenter,
                                               comment_content)

        post_storage_mock.get_comment_id.assert_called_once_with(reply_id)
        post_storage_mock.create_reply.assert_called_once_with(comment_id,
                                                               commenter,
                                                               comment_content)
        presenter_mock.get_create_reply_response.assert_called_once_with(
            comment_id)
        assert response == response_data

    def test_reply_to_comment(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock,
                                                 presenter_mock)

        comment_id = 1
        commenter = 1
        comment_content = "test comment"
        response_data = {"comment_id": 2}
        reply_id = 2

        post_storage_mock.is_comment_or_reply.return_value = True
        post_storage_mock.create_reply.return_value = reply_id
        presenter_mock.get_create_reply_response.return_value = response_data
        response = create_comment.create_reply(comment_id, commenter,
                                               comment_content)

        post_storage_mock.create_reply.assert_called_once_with(comment_id,
                                                               commenter,
                                                               comment_content)
        presenter_mock.get_create_reply_response.assert_called_once_with(
            reply_id)
        assert response == response_data


class TestCreateComment(unittest.TestCase):
    def test_create_comment(self):
        post_storage_mock = Mock(spec=PostStorage)
        presenter_mock = Mock(spec=JsonPresenter)
        create_comment = CreateCommentInteractor(post_storage_mock,
                                                 presenter_mock)

        post_id = 1
        commenter = 1
        comment_content = "test comment"
        response_data = {"comment_id": 1}
        comment_id = 1

        post_storage_mock.create_comment.return_value = comment_id
        presenter_mock.get_create_comment_response.return_value = response_data
        response = create_comment.create_comment(post_id, commenter,
                                                 comment_content)

        post_storage_mock.create_comment.assert_called_once_with(post_id,
                                                                 commenter,
                                                                 comment_content)
        presenter_mock.get_create_comment_response.assert_called_once_with(
            comment_id)
        assert response == response_data
