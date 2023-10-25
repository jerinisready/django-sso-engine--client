from django.urls import path, include

from apps.users.views import login_page, sso_callback

urlpatterns = [
    path('', login_page, name="login"),
    path('oauth/redirect/', sso_callback, name="sso_callback"),
]

