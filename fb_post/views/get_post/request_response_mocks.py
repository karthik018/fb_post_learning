


RESPONSE_200_JSON = """
{
    "postid": 1,
    "posted_by": {
        "userid": 1,
        "username": "string",
        "profile_pic": "string"
    },
    "post_content": "string",
    "post_create_date": "2099-12-31 00:00:00",
    "reactions": {
        "count": 1,
        "types": [
            {
                "reaction": "LIKE"
            }
        ]
    },
    "comment_count": 1,
    "comments": [
        {
            "comment_id": 1,
            "commenter": {
                "userid": 1,
                "username": "string",
                "profile_pic": "string"
            },
            "comment_message": "string",
            "comment_create_date": "2099-12-31 00:00:00",
            "reactions": {
                "count": 1,
                "types": [
                    {
                        "reaction": "LIKE"
                    }
                ]
            },
            "replies_count": 1,
            "replies": [
                {
                    "comment_id": 1,
                    "commenter": {
                        "userid": 1,
                        "username": "string",
                        "profile_pic": "string"
                    },
                    "comment_message": "string",
                    "comment_create_date": "2099-12-31 00:00:00",
                    "reactions": {
                        "count": 1,
                        "types": [
                            {
                                "reaction": "LIKE"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
"""

