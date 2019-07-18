# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "create_person"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/create/"

from .test_case_01 import TestCase01CreatePersonAPITestCase

__all__ = [
    "TestCase01CreatePersonAPITestCase"
]
