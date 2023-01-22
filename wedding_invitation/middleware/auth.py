from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.http import Http404


class AuthMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path == "/admin/" or request.path == "/admin/login/":
            return response

        if request.path != "/login/" and not request.user.is_authenticated:
            raise Http404("ページがありません。")
        return response
