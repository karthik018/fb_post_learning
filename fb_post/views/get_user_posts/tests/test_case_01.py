"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *
from freezegun import freeze_time

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {"username": "ibgroup"},
        "query_params": {"offset": 0, "limit": 2},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    }
}


class TestCase01GetUserPostsAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        self.bar_user = self._create_user("userbar", 'password')
        user_id = self.foo_user.id
        user_id_2 = self.bar_user.id
        self.post1 = Post.objects.create(user_id=user_id, post_description="first post")
        self.post2 = Post.objects.create(user_id=user_id, post_description="second post")
        self.post3 = Post.objects.create(user_id=user_id, post_description="third post")
        self.post4 = Post.objects.create(user_id=user_id_2, post_description="fourth post")

    @freeze_time("2012-03-26")
    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['username'] = self.foo_user.id
        self.default_test_case()
