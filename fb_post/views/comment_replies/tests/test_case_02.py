"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *
from django_swagger_utils.drf_server.exceptions import BadRequest

REQUEST_BODY = """

"""

RESPONSE_BODY = """
{
    "response": "Invalid comment id", "http_status_code": 400, "res_status": "INVALID_COMMENT_ID"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup", "commentid": "ibgroup"},
        "query_params": {"offset": 0, "limit": 2},
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


class TestCase02CommentRepliesAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase02CommentRepliesAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX,
                                                                  TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        user_id = self.foo_user.id
        self.post = Post.objects.create(user_id=user_id, post_description="First post")
        self.comment1 = Comment.objects.create(post_id=self.post.id, user_id=user_id, message="first comment")
        self.comment2 = Comment.objects.create(post_id=self.post.id, user_id=user_id, message="second comment")
        self.reply1_comment1 = Comment.objects.create(post_id=self.post.id, user_id=user_id, commented_on_id=self.comment1, message="first reply to first comment")
        self.reply2_comment1 = Comment.objects.create(post_id=self.post.id, user_id=user_id,
                                                      commented_on_id=self.comment1,
                                                      message="second reply to first comment")
        self.reply1_comment2 = Comment.objects.create(post_id=self.post.id, user_id=user_id,
                                                      commented_on_id=self.comment2,
                                                      message="first reply to second comment")
        self.reply2_comment2 = Comment.objects.create(post_id=self.post.id, user_id=user_id,
                                                      commented_on_id=self.comment2,
                                                      message="second reply to second comment")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        TEST_CASE['request']['path_params']['commentid'] = self.reply1_comment1.id
        super(TestCase02CommentRepliesAPITestCase, self).test_case()
