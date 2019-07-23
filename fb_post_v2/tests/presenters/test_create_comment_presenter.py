from fb_post_v2.interactors.storages.post_storage import CommentIdDTO
from fb_post_v2.presenters.presenter import JsonPresenter
class TestCreateComment:

    def test_create_comment(self):
        presenter = JsonPresenter()

        comment_id_dto = CommentIdDTO(comment_id=1)

        response = presenter.create_comment(comment_dto=comment_id_dto)

        assert response["comment_id"] == comment_id_dto.comment_id
