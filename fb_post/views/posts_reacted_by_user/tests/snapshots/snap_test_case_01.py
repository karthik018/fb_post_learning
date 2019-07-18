# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01PostsReactedByUserAPITestCase::test_case status'] = 200

snapshots['TestCase01PostsReactedByUserAPITestCase::test_case body'] = {
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
                'username': 'user1'
            },
            'postid': 1,
            'reactions': {
                'count': 3,
                'types': [
                    {
                        'reaction': 'LIKE'
                    },
                    {
                        'reaction': 'SAD'
                    },
                    {
                        'reaction': 'HAHA'
                    }
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
                'userid': 2,
                'username': 'user2'
            },
            'postid': 2,
            'reactions': {
                'count': 3,
                'types': [
                    {
                        'reaction': 'LOVE'
                    },
                    {
                        'reaction': 'WOW'
                    },
                    {
                        'reaction': 'WOW'
                    }
                ]
            }
        },
        {
            'comment_count': 0,
            'comments': [
            ],
            'post_content': 'third post',
            'post_create_date': '2012-03-26 00:00:00',
            'posted_by': {
                'profile_pic': '',
                'userid': 3,
                'username': 'user3'
            },
            'postid': 3,
            'reactions': {
                'count': 3,
                'types': [
                    {
                        'reaction': 'SAD'
                    },
                    {
                        'reaction': 'ANGRY'
                    },
                    {
                        'reaction': 'WOW'
                    }
                ]
            }
        }
    ]
}

snapshots['TestCase01PostsReactedByUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '815',
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
