"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup"},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    }
}


class TestCase01GetPostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        self.bar_user = self._create_user("user2", "password")
        self.post = Post.objects.create(user_id=self.foo_user.id, post_description="First post")
        self.comment1 = Comment.objects.create(post_id=self.post.id, user_id=self.foo_user.id, message="first comment")
        self.comment2 = Comment.objects.create(post_id=self.post.id, user_id=self.bar_user.id, message="second comment")
        self.reaction1 = PostReaction.objects.create(post_id=self.post.id, user_id=self.foo_user.id, reaction="LIKE")
        self.reaction2 = PostReaction.objects.create(post_id=self.post.id, user_id=self.bar_user.id, reaction="LOVE")
        self.reply1 = Comment.objects.create(post_id=self.post.id, user_id=self.foo_user.id, commented_on_id=self.comment1, message="first reply")
        self.reply2 = Comment.objects.create(post_id=self.post.id, user_id=self.bar_user.id, commented_on_id=self.comment2, message="second reply")
        self.comment_reaction1 = CommentReaction.objects.create(comment_id=self.comment1.id, user_id=self.foo_user.id, reaction="WOW")
        self.comment_reaction2 = CommentReaction.objects.create(comment_id=self.comment2.id, user_id=self.bar_user.id, reaction="HAHA")

    @freeze_time("2012-03-26")
    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        self.default_test_case()

