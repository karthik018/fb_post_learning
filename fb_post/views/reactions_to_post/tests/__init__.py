# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "reactions_to_post"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{postid}/reactions/"

from .test_case_01 import TestCase01ReactionsToPostAPITestCase

__all__ = [
    "TestCase01ReactionsToPostAPITestCase"
]
