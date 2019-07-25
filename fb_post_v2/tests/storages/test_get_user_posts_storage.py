import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestUserPosts:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")
        self.post2 = Post.objects.create(user_id=self.user.id,
                                         post_description="second post")
        self.post3 = Post.objects.create(user_id=self.user.id,
                                         post_description="third post")
        self.second_user = User.objects.create(username="Manoj",
                                               profile_pic="http://manoj.png")
        self.post4 = Post.objects.create(user_id=self.second_user.id,
                                         post_description="first post")

    def test_user_posts(self, setup_data):
        post_storage = PostStorage()

        userposts_dto = post_storage.get_user_posts(user_id=self.user.id,
                                                    offset=0, limit=2)

        assert len(userposts_dto.posts) == 2

        post_ids = [userpost.post.id for userpost in userposts_dto.posts]

        assert self.post.id in post_ids
        assert self.post2.id in post_ids
        assert self.post3.id not in post_ids
        assert self.post4.id not in post_ids
