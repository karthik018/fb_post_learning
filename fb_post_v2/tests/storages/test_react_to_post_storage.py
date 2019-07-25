import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestReactPost:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")

    def test_react_to_post(self, setup_data):
        post_storage = Storage()
        reaction = "LIKE"

        reaction_id = post_storage.add_post_reaction(self.post.id,
                                                         self.user.id, reaction)

        react = PostReaction.objects.get(id=reaction_id)

        assert reaction_id == react.id
        assert react.post_id == self.post.id
        assert react.reaction == reaction


@pytest.mark.django_db
class TestReactComment:
    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")
        self.first_comment = Comment.objects.create(post_id=self.post.id,
                                                    user_id=self.user.id,
                                                    message="first comment")

    def test_react_to_comment(self, setup_data):
        post_storage = Storage()
        reaction = "LOVE"

        reaction_id = post_storage.add_comment_reaction(
            self.first_comment.id, self.user.id, reaction)

        react = CommentReaction.objects.get(id=reaction_id)

        assert reaction_id == react.id
        assert react.comment_id == self.first_comment.id
        assert react.reaction == reaction
