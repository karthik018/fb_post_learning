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
    "postid": 1,
    "posted_by": {
        "userid": 1,
        "username": "string",
        "profile_pic": "string"
    },
    "post_content": "string",
    "post_create_date": "2099-12-31 00:00:00",
    "reactions": {
        "count": 1,
        "types": [
            {
                "reaction": "LIKE"
            }
        ]
    },
    "comment_count": 1,
    "comments": [
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
            },
            "replies_count": 1,
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
    ]
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"postid": "ibgroup"},
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


class TestCase01GetPostAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01GetPostAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        self.bar_user = self._create_user("user2", "password")
        self.post = Post.objects.create(user_id=self.foo_user.id, post_description="First post")
        self.comment1 = Comment.objects.create(post_id=self.post.id, user_id=self.foo_user.id, message="first comment")
        self.comment2 = Comment.objects.create(post_id=self.post.id, user_id=self.bar_user.id, message="second comment")
        self.reaction1 = PostReaction.objects.create(post_id=self.post.id, user_id=self.foo_user.id, reaction="LIKE")
        self.reaction2 = PostReaction.objects.create(post_id=self.post.id, user_id=self.bar_user.id, reaction="LOVE")
        self.reply1 = Comment.objects.create(post_id=self.post.id, user_id=self.foo_user.id, commented_on_id=self.comment1, message="first reply")
        self.reply2 = Comment.objects.create(post_id=self.post.id, user_id=self.bar_user.id, commented_on_id=self.comment2, message="second reply")
        self.comment_reaction1 = CommentReaction.objects.create(comment_id=self.comment1.id, user_id=self.foo_user.id, reaction="WOW")
        self.comment_reaction2 = CommentReaction.objects.create(comment_id=self.comment2.id, user_id=self.bar_user.id, reaction="HAHA")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['postid'] = self.post.id
        super(TestCase01GetPostAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        import json
        response_data = json.loads(response.content)

        assert response.status_code == 200

        assert response_data['postid'] == self.post.id
        assert response_data['posted_by'] == {"userid": self.foo_user.id, "username": self.foo_user.username, "profile_pic": self.foo_user.profile_pic}
        assert response_data['post_content'] == self.post.post_description
        self.assertDictEqual(response_data['reactions'], {"count": 2, "types": [{"reaction": "LIKE"}, {"reaction": "LOVE"}]})

        assert response_data['comment_count'] == 2
        assert response_data['comments'][0]['comment_id'] == 1
        assert response_data['comments'][1]['comment_id'] == 2
        assert response_data['comments'][0]['commenter'] == {"userid": self.foo_user.id, "username": self.foo_user.username, "profile_pic": self.foo_user.profile_pic}
        assert response_data['comments'][1]['commenter'] == {"userid": self.bar_user.id,
                                                             "username": self.bar_user.username,
                                                             "profile_pic": self.bar_user.profile_pic}
        assert response_data['comments'][0]['comment_message'] == "first comment"
        assert response_data['comments'][1]['comment_message'] == "second comment"
        self.assertDictEqual(response_data['comments'][0]['reactions'], {"count": 1, "types": [{"reaction": "WOW"}]})

        assert response_data['comments'][0]['replies_count'] == 1
        assert response_data['comments'][0]['replies'][0]['comment_id'] == 3
        assert response_data['comments'][0]['replies'][0]['commenter'] == {"userid": self.foo_user.id, "username": self.foo_user.username, "profile_pic": self.foo_user.profile_pic}
        assert response_data['comments'][0]['replies'][0]['comment_message'] == "first reply"
        self.assertDictEqual(response_data['comments'][0]['replies'][0]['reactions'], {"count": 0, "types": []})
