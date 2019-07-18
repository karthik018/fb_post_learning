# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "comment_replies"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{postid}/comment/{commentid}/replies/"

from .test_case_01 import TestCase01CommentRepliesAPITestCase
from .test_case_02 import TestCase02CommentRepliesAPITestCase

__all__ = [
    "TestCase01CommentRepliesAPITestCase",
    "TestCase02CommentRepliesAPITestCase"
]
