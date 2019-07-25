from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.react_interactor import ReactInteractor
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

    interactor = ReactInteractor(post_storage, presenter)

    response = interactor.react_to_comment(comment_id, user.id,
                                           request_data['reaction'])

    import json
    return json.dumps(response)
