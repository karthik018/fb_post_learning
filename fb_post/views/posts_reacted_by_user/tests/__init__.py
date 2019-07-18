# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "posts_reacted_by_user"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/{username}/reacted/posts/"

from .test_case_01 import TestCase01PostsReactedByUserAPITestCase

__all__ = [
    "TestCase01PostsReactedByUserAPITestCase"
]
