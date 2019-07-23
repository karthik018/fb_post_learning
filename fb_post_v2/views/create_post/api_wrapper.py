from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.create_post_interactor import CreatePostInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.presenters.presenter import JsonPresenter

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = kwargs['request_data']

    post_storage = PostStorage()
    presenter = JsonPresenter()

    interactor = CreatePostInteractor(post_storage, presenter)

    response = interactor.create_post(request_data["post_content"], user.id)

    from django.http.response import HttpResponse
    import json
    return HttpResponse(json.dumps(response), status=201)
