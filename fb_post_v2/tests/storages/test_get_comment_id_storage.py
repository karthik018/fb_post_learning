import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestGetCommentId:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")
        self.first_comment = Comment.objects.create(post_id=self.post.id,
                                                    user_id=self.user.id,
                                                    message="first comment")
        self.first_reply = Comment.objects.create(
            post_id=self.post.id, user_id=self.user.id,
            commented_on_id=self.first_comment.id, message="first reply")

    def test_get_comment_id(self, setup_data):
        post_storage = Storage()
        reply_id = self.first_reply.id

        comment_id = post_storage.get_comment_id(reply_id)

        assert comment_id == self.first_comment.id
