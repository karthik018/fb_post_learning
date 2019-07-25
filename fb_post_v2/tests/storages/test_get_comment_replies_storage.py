import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestGetReplies:

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

        self.second_reply = Comment.objects.create(
            post_id=self.post.id, user_id=self.user.id,
            commented_on_id=self.first_comment.id, message="second reply")

    def test_get_replies(self, setup_data):
        post_storage = Storage()

        replies_dto = post_storage.get_comment_replies(self.first_comment.id,
                                                       offset=0, limit=1)

        assert len(replies_dto) == 1

        assert replies_dto[0].comment_id in [self.first_reply.id,
                                             self.second_reply.id]
