from datetime import datetime

from django_swagger_utils.drf_server.exceptions import BadRequest
from freezegun import freeze_time
from fb_post_v2.interactors.storages.post_storage import ReplyDTO, UserDTO
from fb_post_v2.presenters.presenter import Presenter
import pytest


class TestCommentReplies:
    @freeze_time("2012-03-26 00:00:00")
    def test_comment_replies(self):
        presenter = Presenter()
        user = UserDTO(user_id=1, username="karthik", profile_pic="")
        reply_1 = ReplyDTO(comment_id=1, user=user,
                           comment_content="first reply",
                           comment_create_date=datetime.now())

        reply_2 = ReplyDTO(comment_id=2, user=user,
                           comment_content="second reply",
                           comment_create_date=datetime.now())

        replies = [reply_1, reply_2]

        response = presenter.get_comment_replies_response(replies)

        assert len(response["replies"]) == len(replies)

        reply_ids = [reply["comment_id"] for reply in response["replies"]]

        assert reply_1.comment_id in reply_ids
        assert reply_2.comment_id in reply_ids

        test_reply = {}
        for reply in response["replies"]:
            if reply["comment_id"] == reply_1.comment_id:
                test_reply = reply

        assert test_reply["commenter"]["userid"] == user.user_id
        assert test_reply["commenter"]["username"] == user.username
        assert test_reply["comment_message"] == reply_1.comment_content
        assert test_reply["comment_create_date"] == datetime.now().strftime(
                                                    "%Y-%m-%d %H:%M:%S")


class TestRaiseNotComment:

    def test_raise_not_comment(self):
        presenter = Presenter()

        with pytest.raises(BadRequest):
            response = presenter.raise_not_comment()
