"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """
{
    "post_content": "Test_Post_content",
    "post_create_date": "2099-12-31 00:00:00"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    }
}


class TestCase01CreatePostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        self.default_test_case()

    def _assert_snapshots(self, response):
        super(TestCase01CreatePostAPITestCase, self)._assert_snapshots(response)
        import json
        response_data = json.loads(response.content)
        post_id = response_data['postid']
        post = Post.objects.get(id=post_id)

        self.assert_match_snapshot(post.user.id, 'post_user')
        self.assert_match_snapshot(post.post_description, 'post_content')
