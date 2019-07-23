from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.get_reactions_to_post_interactor import GetReactionsToPostInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.presenters.presenter import JsonPresenter

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['postid']
    query_params = kwargs['request_query_params']
    offset = query_params.offset
    limit = query_params.limit

    post_storage = PostStorage()
    presenter = JsonPresenter()

    interactor = GetReactionsToPostInteractor(post_storage, presenter)

    response = interactor.get_reactions_to_post(post_id, offset, limit)

    import json
    return json.dumps(response)
