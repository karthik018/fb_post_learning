from unittest.mock import Mock, patch
import unittest

from django.core.exceptions import ObjectDoesNotExist

from fb_post_v2.interactors.storages.post_storage import ReactionDTO
from fb_post_v2.storages.post_storage import PostStorage

class TestPostReactionExists(unittest.TestCase):
    @patch('fb_post_v2.storages.post_storage.PostReaction')
    def test_post_reaction_exists(self, mock_post_reaction):
        post_storage = PostStorage()
        reaction = Mock()

        id = 1
        post_id = 1
        reacted_by = 1
        reaction.id = id
        reaction.post_id = post_id
        reaction.user_id = reacted_by
        reaction.reaction = "LIKE"

        reaction_dto = ReactionDTO(id=id, react_on_id=post_id, reacted_by=reacted_by, reaction="LIKE")
        mock_post_reaction.objects.get.return_value = reaction
        response = post_storage.post_reaction_exists(post_id, reacted_by)
        print(response)

        assert response == reaction_dto

    @patch('fb_post_v2.storages.post_storage.PostReaction')
    def test_post_reaction_not_exists(self, mock_post_reaction):
        post_storage = PostStorage()

        mock_post_reaction.objects.get.side_effect = ObjectDoesNotExist

        with self.assertRaises(ObjectDoesNotExist):
            response = post_storage.post_reaction_exists(1, 1)

