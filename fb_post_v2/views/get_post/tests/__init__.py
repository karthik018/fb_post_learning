# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "get_post"
REQUEST_METHOD = "get"
URL_SUFFIX = "posts/{postid}/"

from .test_case_01 import TestCase01GetPostAPITestCase

__all__ = [
    "TestCase01GetPostAPITestCase"
]
