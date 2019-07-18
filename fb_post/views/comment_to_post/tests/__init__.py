# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "comment_to_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{postid}/comment/"

from .test_case_01 import TestCase01CommentToPostAPITestCase
from .test_case_02 import TestCase02CommentToPostAPITestCase

__all__ = [
    "TestCase01CommentToPostAPITestCase", "TestCase02CommentToPostAPITestCase"
]
