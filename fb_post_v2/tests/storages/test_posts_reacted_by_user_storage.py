import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestPostsReactedByUser:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")
        self.post2 = Post.objects.create(user_id=self.user.id,
                                         post_description="second post")
        self.first_reaction = PostReaction.objects.create(post_id=self.post.id,
                                                          user_id=self.user.id,
                                                          reaction="LIKE")
        self.second_reaction = PostReaction.objects.create(
            post_id=self.post2.id, user_id=self.user.id,
            reaction="LOVE")

    def test_posts_reacted_by_user(self, setup_data):
        post_storage = PostStorage()

        posts_reacted = post_storage.get_user_reacted_posts(self.user.id)

        assert len(posts_reacted) == 2

        posts_ids = [post_id for post_id in posts_reacted]

        assert self.post.id in posts_ids
        assert self.post2.id in posts_ids
