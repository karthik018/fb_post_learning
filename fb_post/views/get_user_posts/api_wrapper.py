from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import get_user_posts, get_post


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['username']
    query_params = kwargs['request_query_params']
    offset = query_params.offset
    limit = query_params.limit

    post_ids = get_user_posts(user_id=user, offset=offset, limit=limit)

    posts = [get_post(post_id=post_id) for post_id in post_ids]

    response = {"posts": posts}
    return response
