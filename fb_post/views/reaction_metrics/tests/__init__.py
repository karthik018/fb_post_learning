# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "reaction_metrics"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{postid}/reaction/metrics/"

from .test_case_01 import TestCase01ReactionMetricsAPITestCase
from .test_case_02 import TestCase02ReactionMetricsAPITestCase

__all__ = [
    "TestCase01ReactionMetricsAPITestCase",
    "TestCase02ReactionMetricsAPITestCase"
]
