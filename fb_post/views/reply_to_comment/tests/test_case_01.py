"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """
{
    "comment_message": "first reply",
    "comment_create_date": "2099-12-31 00:00:00"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup", "commentid": "ibgroup"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    }
}


class TestCase01ReplyToCommentAPITestCase(CustomAPITestCase):
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
        self.comment = Comment.objects.create(post_id=self.post.id, user_id=user_id, message="first comment")

    @freeze_time("2012-03-26")
    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        TEST_CASE['request']['path_params']['commentid'] = self.comment.id
        self.count_before = Comment.objects.filter(commented_on_id=self.comment.id).count()
        self.default_test_case()

    def _assert_snapshots(self, response):
        super(TestCase01ReplyToCommentAPITestCase, self)._assert_snapshots(response)
        import json
        response_data = json.loads(response.content)
        reply_id = response_data['replyid']
        reply = Comment.objects.get(id=reply_id)

        self.assert_match_snapshot(reply.commented_on_id.id, 'comment_id')
        self.assert_match_snapshot(reply.user.id, 'reply_user')
        self.assert_match_snapshot(reply.post.id, 'reply_post')
        self.assert_match_snapshot(reply.comment_create_date, 'reply_date')
