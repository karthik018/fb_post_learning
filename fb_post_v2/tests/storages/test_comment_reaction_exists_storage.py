from unittest.mock import Mock, patch
import unittest

from django.core.exceptions import ObjectDoesNotExist

from fb_post_v2.interactors.storages.post_storage import ReactionDTO
from fb_post_v2.storages.post_storage import PostStorage

class TestCommentReactionExists(unittest.TestCase):
    @patch('fb_post_v2.storages.post_storage.CommentReaction')
    def test_comment_reaction_exists(self, mock_comment_reaction):
        post_storage = PostStorage()
        reaction = Mock()

        reaction.id = 1
        reaction.comment_id = 1
        reaction.user_id = 1
        reaction.reaction = "LIKE"

        reaction_dto = ReactionDTO(id=1, react_on_id=1, reacted_by=1,
                                   reaction="LIKE")
        mock_comment_reaction.objects.get.return_value = reaction
        response = post_storage.comment_reaction_exists(1, 1)

        assert response == reaction_dto

    @patch('fb_post_v2.storages.post_storage.CommentReaction')
    def test_comment_reaction_not_exists(self, mock_comment_reaction):
        post_storage = PostStorage()

        mock_comment_reaction.objects.get.side_effect = ObjectDoesNotExist

        with self.assertRaises(ObjectDoesNotExist):
            response = post_storage.comment_reaction_exists(1, 1)
