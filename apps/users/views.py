from django.conf import settings
from django.shortcuts import render

from ssoengine.service import DjSSO


# Create your views here.


def login_page(request):
    cxt = {
        'sso_authentication_route': DjSSO(settings.DJ_SSO_API_KEY).authentication_route
    }
    return render(request, 'index.html', cxt)


