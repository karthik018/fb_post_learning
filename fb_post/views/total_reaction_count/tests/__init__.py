# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "total_reaction_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "total/reaction/count/"

from .test_case_01 import TestCase01TotalReactionCountAPITestCase

__all__ = [
    "TestCase01TotalReactionCountAPITestCase"
]
