# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CommentRepliesAPITestCase::test_case reply_count'] = 2

snapshots['TestCase01CommentRepliesAPITestCase::test_case reply_1_id'] = 3

snapshots['TestCase01CommentRepliesAPITestCase::test_case reply_2_id'] = 4

snapshots['TestCase01CommentRepliesAPITestCase::test_case status'] = 200

snapshots['TestCase01CommentRepliesAPITestCase::test_case body'] = {
    'replies': [
        {
            'comment_create_date': '2012-03-26 00:00:00',
            'comment_id': 3,
            'comment_message': 'first reply to first comment',
            'commenter': {
                'profile_pic': '',
                'userid': 1,
                'username': 'username'
            },
            'reactions': None
        },
        {
            'comment_create_date': '2012-03-26 00:00:00',
            'comment_id': 4,
            'comment_message': 'second reply to first comment',
            'commenter': {
                'profile_pic': '',
                'userid': 1,
                'username': 'username'
            },
            'reactions': None
        }
    ]
}

snapshots['TestCase01CommentRepliesAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '396',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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
