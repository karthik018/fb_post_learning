from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """
{
    "comment_message": "test 02 comment to a post",
    "comment_create_date": "2099-12-31 00:00:00"
}
"""

RESPONSE_BODY = """
{
    "commentid": 3
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
    },
    "response": {
        "status": 200,
        "body": RESPONSE_BODY,
        "header_params": {}
    }
}


class TestCase02CommentToPostAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase02CommentToPostAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX,
                                                                 TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        user_id = self.foo_user.id
        self.post = Post.objects.create(user_id=user_id, post_description="Test post for comments")
        self.first_comment = Comment.objects.create(post_id=self.post.id, user_id=self.foo_user.id, message="first_test_comment")
        self.second_comment = Comment.objects.create(post_id=self.post.id, user_id=self.foo_user.id, message="second_test_comment")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        self.count_before = Comment.objects.filter(post_id=self.post.id).count()
        super(TestCase02CommentToPostAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        super(TestCase02CommentToPostAPITestCase, self).compareResponse(response, test_case_response_dict)
        import json
        response_data = json.loads(response.content)
        count_after = Comment.objects.filter(post_id=self.post.id).count()
        comment = Comment.objects.get(id=response_data['commentid'])

        assert count_after == self.count_before + 1
        assert comment.message == "test 02 comment to a post"
        assert comment.post.id == self.post.id
        assert comment.user.id == self.foo_user.id

