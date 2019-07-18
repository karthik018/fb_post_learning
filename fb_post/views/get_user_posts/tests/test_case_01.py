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


class TestCase01GetUserPostsAPITestCase(CustomAPITestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase01GetUserPostsAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE, *args, **kwargs)

    def setupUser(self, username, password):
        pass

    def setup_data(self):
        self.foo_user = self._create_user("username", "password")
        self.bar_user = self._create_user("userbar", 'password')
        user_id = self.foo_user.id
        user_id_2 = self.bar_user.id
        self.post1 = Post.objects.create(user_id=user_id, post_description="first post")
        self.post2 = Post.objects.create(user_id=user_id, post_description="second post")
        self.post3 = Post.objects.create(user_id=user_id, post_description="third post")
        self.post4 = Post.objects.create(user_id=user_id_2, post_description="fourth post")

    def test_case(self):
        self.setup_data()
        TEST_CASE['request']['path_params']['username'] = self.foo_user.id
        super(TestCase01GetUserPostsAPITestCase, self).test_case()

    def compareResponse(self, response, test_case_response_dict):
        import json
        response_data = json.loads(response.content)

        first_user_posts = [post["postid"] for post in response_data['posts']]

        assert len(response_data['posts']) == 2
        assert response_data['posts'][0]['posted_by']['userid'] == self.foo_user.id
        assert response_data['posts'][1]['posted_by']['userid'] == self.foo_user.id
        assert response.status_code == 200
        assert self.post4.id not in first_user_posts




