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
    "total_count": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
    "response": {
        "status": 200,
        "body": RESPONSE_BODY,
        "header_params": {}
    }
}


class TestCase01TotalReactionCountAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01TotalReactionCountAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("user1", "password")
        self.bar_user = self._create_user("user2", "password")
        self.post1 = Post.objects.create(user_id=self.foo_user.id, post_description="first post")
        self.post2 = Post.objects.create(user_id=self.bar_user.id, post_description="second post")
        self.react1_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.foo_user.id, reaction="LIKE")
        self.react1_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.foo_user.id, reaction="LOVE")
        self.react2_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.bar_user.id, reaction="HAHA")
        self.react2_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.bar_user.id, reaction="WOW")

    def test_case(self):
        self.setup_data()
        super(TestCase01TotalReactionCountAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        import json
        response_data = json.loads(response.content)

        expected_count = PostReaction.objects.count()
        total_count = response_data['total_count']

        assert total_count == expected_count
        assert response.status_code == 200
