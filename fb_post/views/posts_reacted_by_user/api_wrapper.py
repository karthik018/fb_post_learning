from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import get_posts_reacted_by_user


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['username']
    posts = get_posts_reacted_by_user(user_id=user)

    response = {"posts": posts}
    return response
