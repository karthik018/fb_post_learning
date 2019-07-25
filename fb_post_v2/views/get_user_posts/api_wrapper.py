from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.get_user_posts_interactor import \
    GetUserPostsInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.presenters.presenter import JsonPresenter


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['username']
    query_params = kwargs['request_query_params']
    offset = query_params.offset
    limit = query_params.limit

    post_storage = PostStorage()
    presenter = JsonPresenter()

    interactor = GetUserPostsInteractor(post_storage, presenter)

    response = interactor.get_user_posts(user, offset, limit)

    import json
    return json.dumps(response)
