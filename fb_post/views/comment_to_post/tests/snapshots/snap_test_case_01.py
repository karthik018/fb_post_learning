# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CommentToPostAPITestCase::test_case status'] = 200

snapshots['TestCase01CommentToPostAPITestCase::test_case body'] = {
    'commentid': 1
}

snapshots['TestCase01CommentToPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '16',
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

snapshots['TestCase01CommentToPostAPITestCase::test_case comment_post'] = 1

snapshots['TestCase01CommentToPostAPITestCase::test_case comment_user'] = 1

snapshots['TestCase01CommentToPostAPITestCase::test_case comment_content'] = 'test comment to a post'
