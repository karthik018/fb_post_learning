
from fb_post_v2.presenters.presenter import JsonPresenter

class TestPostsWithPositiveReactions:

    def test_posts_with_more_positive_reactions(self):
        presenter = JsonPresenter()

        post1_id = 1
        post2_id = 2
        post3_id = 3

        posts_ids = [post1_id, post2_id, post3_id]

        response = presenter.get_positive_reaction_posts_response(posts_ids)

        assert len(response["posts"]) == len(posts_ids)

        post_ids = [post["postid"] for post in response["posts"]]

        assert post1_id in post_ids
        assert post3_id in post_ids
