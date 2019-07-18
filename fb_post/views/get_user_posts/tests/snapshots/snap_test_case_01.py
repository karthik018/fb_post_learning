# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserPostsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetUserPostsAPITestCase::test_case body'] = {
    'posts': [
        {
            'comment_count': 0,
            'comments': [
            ],
            'post_content': 'first post',
            'post_create_date': '2012-03-26 00:00:00',
            'posted_by': {
                'profile_pic': '',
                'userid': 1,
                'username': 'username'
            },
            'postid': 1,
            'reactions': {
                'count': 0,
                'types': [
                ]
            }
        },
        {
            'comment_count': 0,
            'comments': [
            ],
            'post_content': 'second post',
            'post_create_date': '2012-03-26 00:00:00',
            'posted_by': {
                'profile_pic': '',
                'userid': 1,
                'username': 'username'
            },
            'postid': 2,
            'reactions': {
                'count': 0,
                'types': [
                ]
            }
        }
    ]
}

snapshots['TestCase01GetUserPostsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '438',
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
