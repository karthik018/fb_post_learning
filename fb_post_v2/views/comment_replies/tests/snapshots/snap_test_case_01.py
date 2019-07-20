# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CommentRepliesAPITestCase::test_case status'] = 200

snapshots['TestCase01CommentRepliesAPITestCase::test_case body'] = {
    'replies': [
        {
            'comment_create_date': '2099-12-31 00:00:00',
            'comment_id': 1,
            'comment_message': 'string',
            'commenter': {
                'profile_pic': 'string',
                'userid': 1,
                'username': 'string'
            },
            'reactions': {
                'count': 1,
                'types': [
                    'string'
                ]
            }
        }
    ]
}

snapshots['TestCase01CommentRepliesAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '212',
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
