from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.create_comment_interactor import \
    CreateCommentInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.presenters.presenter import Presenter


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    comment_id = kwargs['commentid']

    request_data = kwargs['request_data']

    post_storage = Storage()
    presenter = Presenter()

    interactor = CreateCommentInteractor(post_storage, presenter)

    response = interactor.create_reply(comment_id, user.id,
                                       request_data['comment_message'])

    from django.http.response import HttpResponse
    import json
    return HttpResponse(json.dumps(response), status=201)
