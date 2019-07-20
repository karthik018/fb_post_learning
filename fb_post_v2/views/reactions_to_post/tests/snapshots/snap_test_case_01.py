# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ReactionsToPostAPITestCase::test_case status'] = 200

snapshots['TestCase01ReactionsToPostAPITestCase::test_case body'] = {
    'reactions': [
        {
            'profile_pic': 'string',
            'reaction': 'LIKE',
            'userid': 1,
            'username': 'string'
        }
    ]
}

snapshots['TestCase01ReactionsToPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '89',
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
