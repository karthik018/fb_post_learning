from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.operations import react_to_comment


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    comment_id = kwargs['commentid']
    request_data = kwargs['request_data']

    react_id = react_to_comment(user_id=user.id, comment_id=comment_id, reaction_type=request_data['reaction'])

    response = {"reactionid": react_id}
    import json
    return json.dumps(response)
