import pytest
from freezegun import freeze_time
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.models.models import *


@pytest.mark.django_db
class TestGetPost:

    @freeze_time("2012-03-26")
    @pytest.fixture
    def setup_data(self):
        self.user = User.objects.create(username='karthik',
                                        profile_pic='http://karthik.png')
        self.second_user = User.objects.create(username="Manoj",
                                               profile_pic="http://manoj.png")
        self.post = Post.objects.create(user_id=self.user.id,
                                        post_description="first post")
        self.first_comment = Comment.objects.create(post_id=self.post.id,
                                                    user_id=self.user.id,
                                                    message="first comment")
        self.second_comment = Comment.objects.create(post_id=self.post.id,
                                                     user_id=self.second_user.id,
                                                     message="second comment")
        self.first_reply = Comment.objects.create(
            post_id=self.post.id, user_id=self.second_user.id,
            commented_on_id=self.first_comment.id, message="first reply")

        self.second_reply = Comment.objects.create(
            post_id=self.post.id, user_id=self.user.id,
            commented_on_id=self.second_comment.id, message="second reply")

        self.first_reaction = PostReaction.objects.create(post_id=self.post.id,
                                                          user_id=self.user.id,
                                                          reaction="LOVE")

        self.second_reaction = PostReaction.objects.create(
            post_id=self.post.id, user_id=self.second_user.id, reaction="LOVE")

        self.first_comment_reaction = CommentReaction.objects.create(
            comment_id=self.first_comment.id,
            user_id=self.user.id, reaction="LIKE")
        self.first_comment_reaction2 = CommentReaction.objects.create(
            comment_id=self.first_comment.id,
            user_id=self.second_user.id, reaction="LOVE")
        self.second_comment_reaction = CommentReaction.objects.create(
            comment_id=self.first_reply.id,
            user_id=self.second_user.id, reaction="LIKE")

    def test_get_post_post_content(self, setup_data):
        post_storage = Storage()
        get_post_dto = post_storage.get_post(post_id=1)

        post = get_post_dto.post
        user = get_post_dto.posted_by
        reactions = get_post_dto.reactions

        assert post.id == self.post.id
        assert post.post_content == self.post.post_description
        assert post.post_create_date == self.post.post_create_date
        assert user.user_id == self.post.user_id
        assert user.username == self.post.user.username
        assert user.profile_pic == self.post.user.profile_pic
        assert reactions.count == 2
        assert sorted(["LOVE"]) == reactions.types

        comments = get_post_dto.comments

        assert self.first_comment.id in [comment.id for comment in comments]

        test_comment = None
        for comment in comments:
            if comment.id == self.first_comment.id:
                test_comment = comment

        commenter = test_comment.user
        assert commenter.user_id == self.first_comment.user_id
        assert commenter.username == self.first_comment.user.username
        assert commenter.profile_pic == self.first_comment.user.profile_pic

        assert test_comment.comment_content == self.first_comment.message

        comment_reactions = test_comment.comment_reactions
        assert comment_reactions.count == 2
        assert sorted(comment_reactions.types) == sorted(['LIKE', 'LOVE'])
        assert test_comment.replies_count == 1

        test_reply = None
        for reply in test_comment.replies:
            if reply.id == self.first_reply.id:
                test_reply = reply

        commenter = test_reply.user
        assert commenter.user_id == self.first_reply.user_id
        assert commenter.username == self.first_reply.user.username
        assert commenter.profile_pic == self.first_reply.user.profile_pic

        assert test_reply.comment_content == self.first_reply.message

        reply_reactions = test_reply.comment_reactions
        assert reply_reactions.count == 1
        assert reply_reactions.types == ['LIKE']

    def test_commenter_dto(self, setup_data):
        post_storage = Storage()
        comment = {'id': self.first_comment.id,
                   'user_id': self.first_comment.user_id,
                   'user__username': self.first_comment.user.username,
                   'user__profile_pic': self.first_comment.user.profile_pic,
                   'commented_on_id': self.first_comment.commented_on_id,
                   'comment_create_date':
                       self.first_comment.comment_create_date,
                   'message': self.first_comment.message}

        user_dto = post_storage.get_commenter_dto(comment)

        assert user_dto.user_id == comment['user_id']
        assert user_dto.username == comment['user__username']
        assert user_dto.profile_pic == comment['user__profile_pic']

    def test_comment_reactions_dto(self, setup_data):
        post_storage = Storage()
        comment_reactions = {
            self.first_comment.id: {'count': 2, 'types': ['LIKE', 'LOVE']}}

        reaction_dto = post_storage.get_comment_reactions_dto(
            self.first_comment.id, comment_reactions)

        assert reaction_dto.count == comment_reactions[self.first_comment.id][
            'count']
        assert sorted(reaction_dto.types) == sorted(
            comment_reactions[self.first_comment.id]['types'])

    def test_all_comment_reactions(self, setup_data):
        post_storage = Storage()
        all_comment_reactions = [
            {'comment_id': self.first_comment.id, 'reaction': 'LIKE'},
            {'comment_id': self.first_comment.id, 'reaction': 'LOVE'},
        ]

        comment_reactions = post_storage.get_all_comment_reactions_dict(
            all_comment_reactions)

        assert comment_reactions[self.first_comment.id]['count'] == len(
            all_comment_reactions)
        assert comment_reactions[self.first_comment.id]['types'] == {
            all_comment_reactions[0]['reaction'],
            all_comment_reactions[1]['reaction']}

    def test_get_comment_dto(self, setup_data):
        post_storage = Storage()
        comment = {'id': self.first_comment.id,
                   'user_id': self.first_comment.user_id,
                   'user__username': self.first_comment.user.username,
                   'user__profile_pic': self.first_comment.user.profile_pic,
                   'message': self.first_comment.message,
                   'comment_create_date': self.first_comment.comment_create_date
                   }

        comment_reactions = {
            self.first_comment.id: {'count': 2, 'types': ['LIKE', 'LOVE']}}

        comment_dto = post_storage.get_comment_dto(comment, comment_reactions)

        assert comment_dto.id == comment['id']
        assert comment_dto.user.user_id == comment['user_id']
        assert comment_dto.comment_content == comment['message']
        assert comment_dto.comment_create_date == comment['comment_create_date']

    def test_get_comment_with_replies_dto(self, setup_data):
        post_storage = Storage()
        post_comments = [
            {'id': self.first_comment.id, 'user_id': self.first_comment.user_id,
             'user__username': self.first_comment.user.username,
             'user__profile_pic': self.first_comment.user.profile_pic,
             'message': self.first_comment.message,
             'comment_create_date': self.first_comment.comment_create_date},
            {'id': self.second_comment.id,
             'user_id': self.second_comment.user_id,
             'user__username': self.second_comment.user.username,
             'user__profile_pic': self.second_comment.user.profile_pic,
             'message': self.second_comment.message,
             'comment_create_date': self.second_comment.comment_create_date}
        ]

        comment_reactions = {
            self.first_comment.id: {'count': 2, 'types': ['LIKE', 'LOVE']}}

        replies_dto = []
        replies_count = 0
        comment_with_replies_dto = post_storage.get_comment_with_replies_dto(
            post_comments[0], comment_reactions, replies_count, replies_dto)

        assert comment_with_replies_dto.id == post_comments[0]['id']
        assert comment_with_replies_dto.user.user_id == post_comments[0][
            'user_id']
        assert comment_with_replies_dto.comment_content == post_comments[0][
            'message']
        assert comment_with_replies_dto.replies == replies_dto
        assert comment_with_replies_dto.replies_count == replies_count

    def test_all_comment_replies(self, setup_data):
        post_storage = Storage()

        replies = [
            {'id': self.first_reply.id, 'user_id': self.first_reply.user_id,
             'user__username': self.first_reply.user.username,
             'user__profile_pic': self.first_reply.user.profile_pic,
             'commented_on_id': self.first_comment.id,
             'message': self.first_reply.message,
             'comment_create_date': self.first_reply.comment_create_date}
        ]

        all_replies = post_storage.get_all_comment_replies_dict(replies)

        assert all_replies[self.first_comment.id] == replies
