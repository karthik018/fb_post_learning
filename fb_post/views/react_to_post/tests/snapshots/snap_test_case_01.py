# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01ReactToPostAPITestCase::test_case status'] = 200

snapshots['TestCase01ReactToPostAPITestCase::test_case body'] = {
    'reactionid': 1
}

snapshots['TestCase01ReactToPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '17',
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

snapshots['TestCase01ReactToPostAPITestCase::test_case reaction_id'] = 1

snapshots['TestCase01ReactToPostAPITestCase::test_case reaction_user'] = GenericRepr("<User: username>")

snapshots['TestCase01ReactToPostAPITestCase::test_case reaction_type'] = 'LIKE'
