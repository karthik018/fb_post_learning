from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import reply_to_comment


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    comment_id = kwargs['commentid']
    request_data = kwargs['request_data']

    reply_id = reply_to_comment(comment_id=comment_id, reply_user_id=user.id, reply_text=request_data['comment_message'])

    response = {"replyid": reply_id}

    from django.http.response import HttpResponse
    import json
    return HttpResponse(json.dumps(response), status=201)
