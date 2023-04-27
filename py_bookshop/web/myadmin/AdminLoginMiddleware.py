from django.shortcuts import render, reverse
from django.http import HttpResponse
import re


class AdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        urllist = [reverse('myadmin_login'), reverse('myadmin_gologin'), reverse('myadmin_check_code')]
        if re.match('/admin/', request.path) and request.path not in urllist:
            if request.session.get('AdminUser', '') == '':
                return HttpResponse(f'<script>alert("请先登陆");location.href="{urllist[0]}"</script>')
        response = self.get_response(request)
        return response
