from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.react_interactor import ReactInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import PostStorage
from fb_post_v2.presenters.presenter import JsonPresenter

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['postid']
    user = kwargs['user']
    request_data = kwargs['request_data']

    post_storage = PostStorage()
    presenter = JsonPresenter()

    interactor = ReactInteractor(post_storage, presenter)

    response = interactor.react_to_post(post_id, user.id,
                                        request_data['reaction'])

    import json
    return json.dumps(response)
