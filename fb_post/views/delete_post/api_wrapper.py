from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import delete_post
from django.core.exceptions import ObjectDoesNotExist


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['postid']

    try:
        delete_post(post_id=post_id)
        from django.http.response import HttpResponse
        return HttpResponse(status=200)
    except ObjectDoesNotExist:
        from django_swagger_utils.drf_server.exceptions import BadRequest
        raise BadRequest('Invalid post id', 'INVALID_POST_ID')