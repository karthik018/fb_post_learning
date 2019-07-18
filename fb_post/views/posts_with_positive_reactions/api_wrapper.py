from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import get_posts_with_more_positive_reactions


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    posts = get_posts_with_more_positive_reactions()

    response = {"posts": posts}

    return response
