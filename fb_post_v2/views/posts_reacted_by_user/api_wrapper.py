from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.get_posts_reacted_by_user_interactor import \
    GetPostsReactedByUserInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.presenters.presenter import Presenter

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['username']

    post_storage = Storage()
    presenter = Presenter()

    interactor = GetPostsReactedByUserInteractor(post_storage, presenter)

    response = interactor.get_posts_reacted_by_user(user)

    import json
    return json.dumps(response)
