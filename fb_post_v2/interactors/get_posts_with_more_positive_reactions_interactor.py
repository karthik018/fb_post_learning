from fb_post_v2.interactors.presenters.json_presenter import JsonPresenter
from fb_post_v2.interactors.storages.post_storage import PostStorage

class GetPostsWithPositiveReactionsInteractor:

    def __init__(self, post_storage: PostStorage, presenter: JsonPresenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def get_posts_with_more_positive_reactions(self):
        posts_dto = self.post_storage.get_posts_with_more_positive_reactions()
        response = self.presenter.get_posts_with_more_positive_reactions(posts_dto)
        return response
