"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup", "commentid": "ibgroup"},
        "query_params": {"offset": 0, "limit": 2},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    }
}


class TestCase01CommentRepliesAPITestCase(CustomAPITestCase):
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
        self.default_test_case()

    def _assert_snapshots(self, response):
        import json
        response_data = json.loads(response.content)
        replies = response_data['replies']

        self.assert_match_snapshot(len(replies), 'reply_count')
        self.assert_match_snapshot(replies[0]['comment_id'], 'reply_1_id')
        self.assert_match_snapshot(replies[1]['comment_id'], 'reply_2_id')
