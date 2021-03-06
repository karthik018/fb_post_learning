# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01ReplyToCommentAPITestCase::test_case status'] = 201

snapshots['TestCase01ReplyToCommentAPITestCase::test_case body'] = {
    'replyid': 2
}

snapshots['TestCase01ReplyToCommentAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '14',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01ReplyToCommentAPITestCase::test_case comment_id'] = 1

snapshots['TestCase01ReplyToCommentAPITestCase::test_case reply_user'] = 1

snapshots['TestCase01ReplyToCommentAPITestCase::test_case reply_post'] = 1

snapshots['TestCase01ReplyToCommentAPITestCase::test_case reply_date'] = GenericRepr("FakeDatetime(2012, 3, 26, 0, 0)")
