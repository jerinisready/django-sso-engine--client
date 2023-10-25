from django.urls import path, include

from apps.users.views import login_page

urlpatterns = [
    path('', login_page, name="login")
]

