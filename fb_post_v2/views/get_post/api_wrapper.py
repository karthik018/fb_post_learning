from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.get_post_interactor import GetPostInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.presenters.presenter import Presenter

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['postid']

    post_storage = Storage()
    presenter = Presenter()

    interactor = GetPostInteractor(post_storage, presenter)

    response = interactor.get_post(post_id)

    import json
    return json.dumps(response)
