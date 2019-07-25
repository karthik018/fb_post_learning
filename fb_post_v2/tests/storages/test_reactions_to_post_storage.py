import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestReactionsToPost:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.second_user = User.objects.create(username="Manoj",
                                               profile_pic="http://manoj.png")
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")
        self.first_reaction = PostReaction.objects.create(post_id=self.post.id,
                                                          user_id=self.user.id,
                                                          reaction="LIKE")
        self.second_reaction = PostReaction.objects.create(
            post_id=self.post.id, user_id=self.second_user.id, reaction="LOVE")

    def test_reactions_to_post(self, setup_data):
        post_storage = Storage()

        reactions = post_storage.get_post_reactions(self.post.id, offset=0,
                                                    limit=2)

        assert len(reactions) == 2

        reactions = [reaction_dto.reaction for reaction_dto in reactions]

        assert self.first_reaction.reaction in reactions
        assert self.second_reaction.reaction in reactions
