import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestReactionMetrics:
    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.second_user = User.objects.create(username='Manoj',
                                               profile_pic="http://manoj.png")
        self.third_user = User.objects.create(username='Bharat')
        self.fourth_user = User.objects.create(username='Krishna')
        self.first_post = Post.objects.create(user_id=self.user.id,
                                              post_description="first post")
        self.second_post = Post.objects.create(user_id=self.user.id,
                                               post_description="second post")
        PostReaction.objects.create(user_id=self.user.id,
                                    post_id=self.first_post.id, reaction="LIKE")
        PostReaction.objects.create(user_id=self.second_user.id,
                                    post_id=self.first_post.id, reaction="LOVE")
        PostReaction.objects.create(user_id=self.third_user.id,
                                    post_id=self.first_post.id, reaction="HAHA")
        PostReaction.objects.create(user_id=self.fourth_user.id,
                                    post_id=self.first_post.id, reaction="SAD")
        PostReaction.objects.create(user_id=self.user.id,
                                    post_id=self.second_post.id, reaction="WOW")
        PostReaction.objects.create(user_id=self.second_user.id,
                                    post_id=self.second_post.id, reaction="SAD")
        PostReaction.objects.create(user_id=self.third_user.id,
                                    post_id=self.second_post.id,
                                    reaction="ANGRY")
        PostReaction.objects.create(user_id=self.fourth_user.id,
                                    post_id=self.second_post.id, reaction="SAD")

    def test_reaction_metrics(self, setup_data):
        post_storage = Storage()

        reaction_metrics = post_storage.get_reaction_metrics(self.first_post.id)

        reactions = [[reaction_dto.count, reaction_dto.reaction] for
                     reaction_dto in reaction_metrics]

        assert [1, 'LIKE'] in reactions
        assert [1, 'LOVE'] in reactions
        assert [1, 'HAHA'] in reactions
        assert [1, 'SAD'] in reactions
