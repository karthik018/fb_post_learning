# pylint: disable=wrong-import-position

APP_NAME = "fb_post_v2"
OPERATION_NAME = "posts_with_positive_reactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/positive/reactions/"

from .test_case_01 import TestCase01PostsWithPositiveReactionsAPITestCase

__all__ = [
    "TestCase01PostsWithPositiveReactionsAPITestCase"
]
