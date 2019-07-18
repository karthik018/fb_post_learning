"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.models import *

REQUEST_BODY = """
{
    "reaction": "LIKE"
}
"""

RESPONSE_BODY = """
{
    "reactionid": 1
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
        "status": 200,
        "body": RESPONSE_BODY,
        "header_params": {}
    }
}


class TestCase02ReactToCommentAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase02ReactToCommentAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        user_id = self.foo_user.id
        self.post = Post.objects.create(user_id=user_id, post_description="First post")
        self.comment = Comment.objects.create(user_id=user_id, post_id=self.post.id, message="first comment")
        self.react = CommentReaction.objects.create(user_id=user_id, comment_id=self.comment.id, reaction="LOVE")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        TEST_CASE['request']['path_params']['commentid'] = self.comment.id
        self.count_before = CommentReaction.objects.filter(user_id=self.foo_user.id, comment_id=self.comment.id).count()
        super(TestCase02ReactToCommentAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        import json
        response_data = json.loads(response.content)
        count_after = CommentReaction.objects.filter(user_id=self.foo_user.id, comment_id=self.comment.id).count()
        reaction_id = response_data['reactionid']
        reaction = CommentReaction.objects.get(user_id=self.foo_user.id, comment_id=self.comment.id)
        assert count_after == self.count_before
        assert reaction.id == reaction_id
        assert reaction.user == self.foo_user
        assert reaction.reaction == "LIKE"
