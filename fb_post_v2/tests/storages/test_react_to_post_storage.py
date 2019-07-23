import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.models.models import *

@pytest.mark.django_db
class TestReactPost:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik', profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id, post_description="first post")

    def test_react_to_post(self, setup_data):
        post_storage = PostStorage()
        reaction = "LIKE"

        reaction_id_dto = post_storage.react_to_post(self.post.id, self.user.id, reaction)

        react = PostReaction.objects.get(id=reaction_id_dto.reaction_id)

        assert reaction_id_dto.reaction_id == 1
        assert react.post_id == self.post.id
        assert react.reaction == reaction


@pytest.mark.django_db
class TestReactComment:
    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik', profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id, post_description="first post")
        self.first_comment = Comment.objects.create(post_id=self.post.id, user_id=self.user.id, message="first comment")

    def test_react_to_comment(self, setup_data):
        post_storage = PostStorage()
        reaction = "LOVE"

        reaction_id_dto = post_storage.react_to_comment(self.first_comment.id, self.user.id, reaction)

        react = CommentReaction.objects.get(id=reaction_id_dto.reaction_id)

        assert reaction_id_dto.reaction_id == 1
        assert react.comment_id == self.first_comment.id
        assert react.reaction == reaction

