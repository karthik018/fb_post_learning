import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestTotalReactionCount:

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
        PostReaction.objects.create(user_id=self.user.id,
                                    post_id=self.first_post.id, reaction="LIKE")
        PostReaction.objects.create(user_id=self.second_user.id,
                                    post_id=self.first_post.id, reaction="LOVE")
        PostReaction.objects.create(user_id=self.third_user.id,
                                    post_id=self.first_post.id, reaction="HAHA")
        PostReaction.objects.create(user_id=self.fourth_user.id,
                                    post_id=self.first_post.id, reaction="SAD")

    def test_total_reaction_count(self, setup_data):
        post_storage = PostStorage()

        count_dto = post_storage.get_total_reaction_count()

        assert count_dto.count == 4
