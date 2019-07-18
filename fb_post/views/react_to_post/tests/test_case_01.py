"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """
{
    "reaction": "LIKE"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    }
}


class TestCase01ReactToPostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        user_id = self.foo_user.id
        self.post = Post.objects.create(user_id=user_id, post_description="First post")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        self.default_test_case()

    def _assert_snapshots(self, response):
        super(TestCase01ReactToPostAPITestCase, self)._assert_snapshots(response)
        reaction = PostReaction.objects.get(user_id=self.foo_user.id, post_id=self.post.id)
        self.assert_match_snapshot(reaction.id, 'reaction_id')
        self.assert_match_snapshot(reaction.user, 'reaction_user')
        self.assert_match_snapshot(reaction.reaction, 'reaction_type')

