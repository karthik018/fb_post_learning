from django.utils.deprecation import MiddlewareMixin


class ExceptionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("view called")
        print(response)

        return response

    # def process_request(self, request):
    #     print("request called in exception mw")

    def process_exception(self, request, exception):
        print("exce called", type(exception))

        from django.http.response import HttpResponse
        import json
        return HttpResponse(json.dumps({"error_message": "bad operation"}),
                            status=400)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("called")
        # from django.http.response import HttpResponse
        # import json
        # return HttpResponse(json.dumps({"error_message": "bad operation"}),
        #                     status=400)
