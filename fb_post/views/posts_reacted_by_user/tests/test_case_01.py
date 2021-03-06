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
        "path_params": {"username": "ibgroup"},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    }
}


class TestCase01PostsReactedByUserAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("user1", "password")
        self.bar_user = self._create_user("user2", "password")
        self.foo_bar_user = self._create_user("user3", "password")
        self.post1 = Post.objects.create(user_id=self.foo_user.id, post_description="first post")
        self.post2 = Post.objects.create(user_id=self.bar_user.id, post_description="second post")
        self.post3 = Post.objects.create(user_id=self.foo_bar_user.id, post_description="third post")
        self.react1_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.foo_user.id, reaction="LIKE")
        self.react1_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.foo_user.id, reaction="LOVE")
        self.react3_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.foo_bar_user.id, reaction="SAD")
        self.react2_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.bar_user.id, reaction="HAHA")
        self.react2_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.bar_user.id, reaction="WOW")
        self.react3_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.foo_bar_user.id, reaction="WOW")
        self.react1_post3 = PostReaction.objects.create(post_id=self.post3.id, user_id=self.foo_bar_user.id, reaction="SAD")
        self.react2_post3 = PostReaction.objects.create(post_id=self.post3.id, user_id=self.foo_user.id, reaction="ANGRY")
        self.react3_post3 = PostReaction.objects.create(post_id=self.post3.id, user_id=self.bar_user.id, reaction="WOW")

    @freeze_time("2012-03-26")
    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['username'] = self.foo_user.id
        self.default_test_case()
