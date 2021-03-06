from unittest.mock import Mock, patch
import unittest

from fb_post_v2.storages.post_storage import Storage

class TestCommentOrReply(unittest.TestCase):
    @patch('fb_post_v2.storages.post_storage.Comment')
    def test_comment(self, mock_comment):
        post_storage = Storage()

        comment_id = 2
        comment = Mock()
        comment.commented_on = None
        mock_comment.objects.get.return_value = comment
        response = post_storage.is_comment_or_reply(comment_id)

        assert response is True

    @patch('fb_post_v2.storages.post_storage.Comment')
    def test_reply(self, mock_comment):
        post_storage = Storage()

        comment_id = 2
        comment = Mock()
        comment.commented_on = 1
        mock_comment.objects.get.return_value = comment
        response = post_storage.is_comment_or_reply(comment_id)

        assert response is False
