from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect

from ssoengine.service import SSOAgent


# Create your views here.


def login_page(request):
    cxt = {
        'sso_authentication_route': SSOAgent(settings.DJ_SSO_API_KEY).authentication_route
    }
    return render(request, 'index.html', cxt)


# def sso_callback_for_other_python_frameworks(request):
#     if request.GET.get('state') != 'SUCCESS':
#         return redirect('login') + "?state=UNVERIFIED"
#     sso = SSOAgent(settings.DJ_SSO_API_KEY, token=request.GET['auth_token'])
#     auth = sso.get_user_details()
#     if auth is None:
#         return JsonResponse({'state': 'UNVERIFIED'}, status=400)
#
#     # ... Handle What ever you want
#     return JsonResponse({'state': 'VERIFIED'})
#

def sso_callback(request):
    if request.GET.get('state') != 'SUCCESS':
        messages.info(request, 'SSO Authentication Failed!')
        return redirect('login')
    sso = SSOAgent(settings.DJ_SSO_API_KEY, token=request.GET['auth_token'])
    user = authenticate(request, sso_agent=sso)
    if user is None:
        return JsonResponse({'state': sso.response_state}, status=400)
    login(request, user)
    return JsonResponse({'state': sso.response_state}, status=200)
