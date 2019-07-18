"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """

"""

RESPONSE_BODY = """
{
    "response": "Invalid post id", "http_status_code": 400, "res_status": "INVALID_POST_ID"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup"},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
    "response": {
        "status": 400,
        "body": RESPONSE_BODY,
        "header_params": {}
    }
}


class TestCase02DeletePostAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase02DeletePostAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        user_id = self.foo_user.id
        self.post = Post.objects.create(user_id=user_id, post_description="First post")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = 2
        super(TestCase02DeletePostAPITestCase, self).test_case()

