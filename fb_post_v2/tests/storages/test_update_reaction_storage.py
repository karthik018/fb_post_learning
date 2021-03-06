import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestUpdatePostReaction:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.second_user = User.objects.create(username='Manoj',
                                               profile_pic="http://manoj.png")
        self.first_post = Post.objects.create(user_id=self.user.id,
                                              post_description="first post")
        self.first_Reaction = PostReaction.objects.create(
            user_id=self.user.id, post_id=self.first_post.id, reaction="LIKE")

    def test_delete_post_reaction(self, setup_data):
        post_storage = Storage()

        reaction_id = post_storage.update_post_reaction(self.first_post.id,
                                                        self.user.id, "LOVE")

        assert reaction_id == self.first_Reaction.id


@pytest.mark.django_db
class TestUpdateCommentReaction:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.second_user = User.objects.create(username='Manoj',
                                               profile_pic="http://manoj.png")
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")
        self.first_comment = Comment.objects.create(post_id=self.post.id,
                                                    user_id=self.user.id,
                                                    message="first comment")
        self.first_comment_reaction = CommentReaction.objects.create(
            comment_id=self.first_comment.id,
            user_id=self.user.id, reaction="LIKE")

    def test_delete_comment_reaction(self, setup_data):
        post_storage = Storage()

        reaction_id = post_storage.update_comment_reaction(
            self.first_comment.id, self.user.id, "LOVE")

        assert reaction_id == self.first_comment_reaction.id
