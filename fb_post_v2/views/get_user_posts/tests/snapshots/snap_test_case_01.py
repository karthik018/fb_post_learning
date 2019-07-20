# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserPostsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetUserPostsAPITestCase::test_case body'] = {
    'posts': [
        {
            'comment_count': 1,
            'comments': [
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
                    },
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
                    ],
                    'replies_count': 1
                }
            ],
            'post_content': 'string',
            'post_create_date': '2099-12-31 00:00:00',
            'posted_by': {
                'profile_pic': 'string',
                'userid': 1,
                'username': 'string'
            },
            'postid': 1,
            'reactions': {
                'count': 1,
                'types': [
                    'string'
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
        '659',
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
