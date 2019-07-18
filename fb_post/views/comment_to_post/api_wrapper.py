from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import add_comment


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = kwargs['request_data']
    post_id = kwargs['postid']

    comment_id = add_comment(post_id=post_id, comment_user_id=user.id, comment_text=request_data['comment_message'])
    response = {"commentid": comment_id}

    from django.http.response import HttpResponse
    import json
    return HttpResponse(json.dumps(response), status=200)
