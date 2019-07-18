"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *
from django.core.exceptions import ObjectDoesNotExist

REQUEST_BODY = """
{
    "reaction": "LOVE"
}
"""

RESPONSE_BODY = """
{
    "reactionid": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
    "response": {
        "status": 200,
        "body": RESPONSE_BODY,
        "header_params": {}
    }
}


class TestCase03ReactToPostAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase03ReactToPostAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        user_id = self.foo_user.id
        self.post = Post.objects.create(user_id=user_id, post_description="First post")
        self.react = PostReaction.objects.create(user_id=user_id, post_id=self.post.id, reaction="LOVE")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        self.count_before = PostReaction.objects.filter(user_id=self.foo_user.id, post_id=self.post.id).count()
        super(TestCase03ReactToPostAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        with self.assertRaises(ObjectDoesNotExist):
            PostReaction.objects.get(user_id=self.foo_user.id, post_id=self.post.id)

