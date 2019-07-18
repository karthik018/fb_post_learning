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
    "replies": [
        {
            "comment_id": 1,
            "commenter": {
                "userid": 1,
                "username": "string",
                "profile_pic": "string"
            },
            "comment_message": "string",
            "comment_create_date": "2099-12-31 00:00:00",
            "reactions": {
                "count": 1,
                "types": [
                    {
                        "reaction": "LIKE"
                    }
                ]
            }
        }
    ]
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
        "status": 200,
        "body": RESPONSE_BODY,
        "header_params": {}
    }
}


class TestCase01CommentRepliesAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01CommentRepliesAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX,
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
        TEST_CASE['request']['path_params']['commentid'] = self.comment1.id
        super(TestCase01CommentRepliesAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        import json
        response_data = json.loads(response.content)
        replies = response_data['replies']

        assert len(replies) == 2
        assert replies[0]['comment_id'] == 3
        assert replies[1]['comment_id'] == 4
        assert response.status_code == 200

