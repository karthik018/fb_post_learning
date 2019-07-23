import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.models.models import *

@pytest.mark.django_db
class TestCreatePost:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik', profile_pic='http://karthik.png')

    def test_create_post(self, setup_data):
        post_storage = PostStorage()
        post_content = "first post"

        post_id_dto = post_storage.create_post(post_content, self.user.id)

        post = Post.objects.get(id=post_id_dto.post_id)

        assert post_id_dto.post_id == 1
        assert post.post_description == post_content

