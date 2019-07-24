from fb_post_v2.interactors.storages.post_storage import CommentIdDTO
from fb_post_v2.presenters.presenter import JsonPresenter

class TestCreateReply:

    def test_create_reply(self):
        presenter = JsonPresenter()

        comment_id_dto = CommentIdDTO(comment_id=1)

        response = presenter.get_create_reply_response(comment_id_dto)

        assert response["reply_id"] == comment_id_dto.comment_id
