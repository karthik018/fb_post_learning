from fb_post_v2.interactors.storages.post_storage import PostIdDTO
from fb_post_v2.presenters.presenter import JsonPresenter

class TestPostsReactedByUser:

    def test_posts_reacted_by_user(self):

        presenter = JsonPresenter()

        post1_id_dto = PostIdDTO(post_id=1)
        post2_id_dto = PostIdDTO(post_id=2)
        post3_id_dto = PostIdDTO(post_id=3)

        posts_dto = [post1_id_dto, post2_id_dto, post3_id_dto]

        response = presenter.get_posts_reacted_by_user_response(posts_dto)

        assert len(response["posts"]) == len(posts_dto)

        post_ids = [post["postid"] for post in response["posts"]]

        assert post1_id_dto.post_id in post_ids
        assert post3_id_dto.post_id in post_ids
