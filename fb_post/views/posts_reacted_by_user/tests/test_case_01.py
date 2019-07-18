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
    "posts": [
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
    ]
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"username": "ibgroup"},
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


class TestCase01PostsReactedByUserAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01PostsReactedByUserAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("user1", "password")
        self.bar_user = self._create_user("user2", "password")
        self.foo_bar_user = self._create_user("user3", "password")
        self.post1 = Post.objects.create(user_id=self.foo_user.id, post_description="first post")
        self.post2 = Post.objects.create(user_id=self.bar_user.id, post_description="second post")
        self.post3 = Post.objects.create(user_id=self.foo_bar_user.id, post_description="third post")
        self.react1_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.foo_user.id, reaction="LIKE")
        self.react1_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.foo_user.id, reaction="LOVE")
        self.react3_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.foo_bar_user.id, reaction="SAD")
        self.react2_post1 = PostReaction.objects.create(post_id=self.post1.id, user_id=self.bar_user.id, reaction="HAHA")
        self.react2_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.bar_user.id, reaction="WOW")
        self.react3_post2 = PostReaction.objects.create(post_id=self.post2.id, user_id=self.foo_bar_user.id, reaction="WOW")
        self.react1_post3 = PostReaction.objects.create(post_id=self.post3.id, user_id=self.foo_bar_user.id, reaction="SAD")
        self.react2_post3 = PostReaction.objects.create(post_id=self.post3.id, user_id=self.foo_user.id, reaction="ANGRY")
        self.react3_post3 = PostReaction.objects.create(post_id=self.post3.id, user_id=self.bar_user.id, reaction="WOW")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['username'] = self.foo_user.id
        super(TestCase01PostsReactedByUserAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        import json
        response_data = json.loads(response.content)
        user_reacted_posts = response_data['posts']
        post_ids = [user_reacted_posts[i]['postid'] for i in range(len(user_reacted_posts))]
        assert len(user_reacted_posts) == 3
        assert self.post1.id in post_ids
        assert self.post2.id in post_ids
        assert self.post3.id in post_ids
        assert response.status_code == 200
