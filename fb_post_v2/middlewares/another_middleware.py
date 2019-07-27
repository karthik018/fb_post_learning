from django.core.exceptions import ObjectDoesNotExist, SuspiciousOperation

from django.utils.deprecation import MiddlewareMixin

class AnotherMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("another_view called")
        # raise SuspiciousOperation()

        return response

    # def process_exception(self, request, exception):
    #     print("another_exce called", type(exception))
    #
    #     from django.http.response import HttpResponse
    #     import json
    #     return HttpResponse(json.dumps({"error_message": "Invalid post id"}),
    #                         status=400)

    # def process_request(self, request):
    #     print("request_called")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("another_p_view_called")
        # from django.http.response import HttpResponse
        # import json
        # return HttpResponse(json.dumps({"error_message": "Invalid"}),
        #                     status=400)
