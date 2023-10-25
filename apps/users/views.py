from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect

from ssoengine.helper import get_or_create_user
from ssoengine.service import DjSSO


# Create your views here.


def login_page(request):
    cxt = {
        'sso_authentication_route': DjSSO(settings.DJ_SSO_API_KEY).authentication_route
    }
    return render(request, 'index.html', cxt)


def sso_callback(request):
    if request.GET.get('state') != 'SUCCESS':
        messages.info(request, 'SSO Authentication Failed!')
        return redirect('login')
    sso = DjSSO(settings.DJ_SSO_API_KEY)
    auth = sso.get_user_details(token=request.GET['auth_token'])
    if auth:
        user = get_or_create_user(auth)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return JsonResponse({'state': 'VERIFIED'})
    return JsonResponse({'state': 'UNVERIFIED'}, status=400)
