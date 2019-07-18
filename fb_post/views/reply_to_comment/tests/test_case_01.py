"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """
{
    "comment_message": "first reply",
    "comment_create_date": "2099-12-31 00:00:00"
}
"""

RESPONSE_BODY = """
{
    "replyid": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup", "commentid": "ibgroup"},
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


class TestCase01ReplyToCommentAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01ReplyToCommentAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        user_id = self.foo_user.id
        self.post = Post.objects.create(user_id=user_id, post_description="First post")
        self.comment = Comment.objects.create(post_id=self.post.id, user_id=user_id, message="first comment")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        TEST_CASE['request']['path_params']['commentid'] = self.comment.id
        self.count_before = Comment.objects.filter(commented_on_id=self.comment.id).count()
        super(TestCase01ReplyToCommentAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        count_after = Comment.objects.filter(commented_on_id=self.comment.id).count()
        import json
        response_date = json.loads(response.content)
        reply_id = response_date['replyid']
        reply = Comment.objects.get(id=reply_id)

        assert count_after == self.count_before + 1
        assert reply_id == 2
        assert reply.commented_on_id.id == self.comment.id
        assert reply.user.id == self.foo_user.id
        assert reply.post.id == self.post.id



