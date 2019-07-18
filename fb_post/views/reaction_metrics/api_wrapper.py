from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import get_reaction_metrics


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['postid']

    reaction_metrics = get_reaction_metrics(post_id=post_id)

    response = {"reactions": reaction_metrics}
    import json
    return json.dumps(response)
