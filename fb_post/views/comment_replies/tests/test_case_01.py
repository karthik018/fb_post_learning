"""
# TODO: Update test case description
"""
from django_swagger_utils.drf_server.utils.server_gen.custom_api_test_case import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

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
        "body": {
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
        },
        "header_params": {}
    }
}


class TestCase01CommentRepliesAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        super(TestCase01CommentRepliesAPITestCase, self).__init__(APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, TEST_CASE)
        super(TestCase01CommentRepliesAPITestCase, self).test_case()
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
