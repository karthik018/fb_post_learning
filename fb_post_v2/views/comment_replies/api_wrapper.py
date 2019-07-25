from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.replies_for_comment_interactor import \
    CommentRepliesInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.presenters.presenter import Presenter


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    comment_id = kwargs['commentid']

    query_params = kwargs['request_query_params']
    offset = query_params.offset
    limit = query_params.limit

    post_storage = Storage()
    presenter = Presenter()

    interactor = CommentRepliesInteractor(post_storage, presenter)

    response = interactor.get_comment_replies(comment_id, offset, limit)

    import json

    return json.dumps(response)

