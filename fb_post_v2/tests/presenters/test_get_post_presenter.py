from datetime import datetime
from freezegun import freeze_time
from fb_post_v2.presenters.presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import UserDTO, PostDTO, ReactionsDTO, GetPostDTO
import pytest

class TestGetPost:
    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        user = UserDTO(user_id=1, username='karthik', profile_pic="")
        post = PostDTO(id=1, post_content="first post", post_create_date=datetime.now())
        post_reaction = ReactionsDTO(count=2, types=["LOVE", "LIKE"])
        comments = []
        comment_count = 0

        self.get_post_dto = GetPostDTO(post, user, post_reaction, comments, comment_count)

    def test_get_post(self, setup_data):
        presenter = JsonPresenter()

        response = presenter.get_post(self.get_post_dto)

        assert response["postid"] == self.get_post_dto.post.id
        assert response["posted_by"]["userid"] == self.get_post_dto.posted_by.user_id
        assert response["posted_by"]["username"] == self.get_post_dto.posted_by.username
        assert response["posted_by"]["profile_pic"] == self.get_post_dto.posted_by.profile_pic

        assert response["post_content"] == self.get_post_dto.post.post_content
        assert response["post_create_date"] == self.get_post_dto.post.post_create_date

        assert response["reactions"]["count"] == self.get_post_dto.reactions.count
        assert response["reactions"]["types"] == self.get_post_dto.reactions.types

        assert response["comment_count"] == self.get_post_dto.comment_count



