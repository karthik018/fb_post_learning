"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
import json
from fb_post.models.models import *


REQUEST_BODY = """
{
    "post_content": "Test_Post_content",
    "post_create_date": "2099-12-31 00:00:00"
}
"""

RESPONSE_BODY = """
{
    "postid": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
    "response": {
        "status": 201,
        "body": RESPONSE_BODY,
        "header_params": {}
    }
}


class TestCase01CreatePostAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01CreatePostAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX,
                                                              TEST_CASE, *args, **kwargs)

    def test_case(self):
        self.count_before = Post.objects.count()
        print(self.count_before)
        super(TestCase01CreatePostAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        super(TestCase01CreatePostAPITestCase, self).compareResponse(response, test_case_response_dict)
        count_after = Post.objects.count()

        response_data = json.loads(response.content)
        post = Post.objects.get(id=response_data["postid"])

        assert post.post_description == "Test_Post_content"
        assert count_after == self.count_before + 1
        assert post.user == self.foo_user
