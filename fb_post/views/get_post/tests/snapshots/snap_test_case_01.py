# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPostAPITestCase::test_case status'] = 200

snapshots['TestCase01GetPostAPITestCase::test_case body'] = {
    'comment_count': 2,
    'comments': [
        {
            'comment_create_date': '2012-03-26 00:00:00',
            'comment_id': 1,
            'comment_message': 'first comment',
            'commenter': {
                'profile_pic': '',
                'userid': 1,
                'username': 'username'
            },
            'reactions': {
                'count': 1,
                'types': [
                    {
                        'reaction': 'WOW'
                    }
                ]
            },
            'replies': [
                {
                    'comment_create_date': '2012-03-26 00:00:00',
                    'comment_id': 3,
                    'comment_message': 'first reply',
                    'commenter': {
                        'profile_pic': '',
                        'userid': 1,
                        'username': 'username'
                    },
                    'reactions': {
                        'count': 0,
                        'types': [
                        ]
                    }
                }
            ],
            'replies_count': 1
        },
        {
            'comment_create_date': '2012-03-26 00:00:00',
            'comment_id': 2,
            'comment_message': 'second comment',
            'commenter': {
                'profile_pic': '',
                'userid': 2,
                'username': 'user2'
            },
            'reactions': {
                'count': 1,
                'types': [
                    {
                        'reaction': 'HAHA'
                    }
                ]
            },
            'replies': [
                {
                    'comment_create_date': '2012-03-26 00:00:00',
                    'comment_id': 4,
                    'comment_message': 'second reply',
                    'commenter': {
                        'profile_pic': '',
                        'userid': 2,
                        'username': 'user2'
                    },
                    'reactions': {
                        'count': 0,
                        'types': [
                        ]
                    }
                }
            ],
            'replies_count': 1
        }
    ],
    'post_content': 'First post',
    'post_create_date': '2012-03-26 00:00:00',
    'posted_by': {
        'profile_pic': '',
        'userid': 1,
        'username': 'username'
    },
    'postid': 1,
    'reactions': {
        'count': 2,
        'types': [
            {
                'reaction': 'LIKE'
            },
            {
                'reaction': 'LOVE'
            }
        ]
    }
}

snapshots['TestCase01GetPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1115',
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
