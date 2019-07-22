from unittest.mock import Mock, patch
import unittest

from django.core.exceptions import ObjectDoesNotExist

from fb_post_v2.storages.post_storage import PostStorage

class TestPostExists(unittest.TestCase):
    @patch('fb_post_v2.storages.post_storage.Post')
    def test_post_exists(self, mock_post):
        post_storage = PostStorage()

        post = Mock()
        mock_post.objects.get.return_value = post
        response = post_storage.post_exists(1)

        assert response is True

    @patch('fb_post_v2.storages.post_storage.Post')
    def test_post_not_exists(self, mock_post):
        post_storage = PostStorage()

        mock_post.objects.get.side_effect = ObjectDoesNotExist
        response = post_storage.post_exists(1)

        assert response is False
