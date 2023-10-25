from django.conf import settings


class DjSSO(object):
    BASE_URL = 'http://localhost:8000'

    def __init__(self, api_key=None):
        self.DJ_SSO_API_KEY = api_key

    @property
    def authentication_route(self):
        return f'{self.BASE_URL}/sso/web/{settings.DJ_SSO_API_KEY}/'



