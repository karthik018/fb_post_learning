import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.models.models import *

@pytest.mark.django_db
class TestCreateComment:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik', profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id, post_description="first post")

    def test_create_comment(self, setup_data):
        post_storage = PostStorage()
        comment_content = "first comment"

        comment_id_dto = post_storage.create_comment(self.post.id, self.user.id, comment_content)

        comment = Comment.objects.get(id=comment_id_dto.comment_id)

        assert comment_id_dto.comment_id == 1
        assert comment.message == comment_content
