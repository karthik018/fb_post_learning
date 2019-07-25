from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.get_total_reaction_count_interactor import \
    GetTotalReactionCountInteractor
from .validator_class import ValidatorClass
from fb_post_v2.storages.post_storage import Storage
from fb_post_v2.presenters.presenter import Presenter

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_storage = Storage()
    presenter = Presenter()

    interactor = GetTotalReactionCountInteractor(post_storage, presenter)

    response = interactor.get_total_reaction_count()

    import json
    return json.dumps(response)
