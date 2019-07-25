import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *

@pytest.mark.django_db
class TestCreatePost:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')

    def test_create_post(self, setup_data):
        post_storage = Storage()
        post_content = "first post"

        post_id = post_storage.create_post(post_content, self.user.id)

        post = Post.objects.get(id=post_id)

        assert post_id == post.id
        assert post.post_description == post_content

