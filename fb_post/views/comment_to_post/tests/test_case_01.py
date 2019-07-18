"""
# TODO: Update test case description
"""
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *
from freezegun import freeze_time

REQUEST_BODY = """
{
    "comment_message": "test comment to a post",
    "comment_create_date": "2099-12-31 00:00:00"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup"},
        "query_params": {},
        "header_params": {},
        "securities": {
            "oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"],
                      "type": "oauth2"}},
        "body": REQUEST_BODY,
    }
}


class TestCase01CommentToPostAPITestCase(CustomAPITestCase):
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
        self.post = Post.objects.create(user_id=user_id, post_description="Test post for comments")

    @freeze_time("2012-03-26")
    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        self.count_before = Comment.objects.filter(post_id=self.post.id).count()
        self.default_test_case()

    def _assert_snapshots(self, response):
        super(TestCase01CommentToPostAPITestCase, self)._assert_snapshots(response)
        import json
        response_data = json.loads(response.content)
        comment_id = response_data['commentid']
        comment = Comment.objects.get(id=comment_id)

        self.assert_match_snapshot(comment.post.id, 'comment_post')
        self.assert_match_snapshot(comment.user.id, 'comment_user')
        self.assert_match_snapshot(comment.message, 'comment_content')
        self.assert_match_snapshot(comment.comment_create_date, 'comment_create_date')
