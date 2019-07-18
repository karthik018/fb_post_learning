from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import get_total_reaction_count


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    total_count = get_total_reaction_count()

    response = {"total_count": total_count}
    import json
    return json.dumps(response)
