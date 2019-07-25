from fb_post_v2.presenters.presenter import JsonPresenter

class TestCreateReply:

    def test_create_reply(self):
        presenter = JsonPresenter()

        reply_id = 2

        response = presenter.get_create_reply_response(reply_id)

        assert response["reply_id"] == reply_id
