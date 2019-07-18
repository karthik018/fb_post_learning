from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import get_post


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['postid']
    response = get_post(post_id=post_id)

    # from django.http.response import HttpResponse
    # return HttpResponse(str(response), status=200)
    return response
