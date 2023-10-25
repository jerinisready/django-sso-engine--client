import requests


class DjSSO(object):
    BASE_URL = 'http://localhost:8000'

    def __init__(self, api_key=None, api_secret=None):
        self.DJ_SSO_API_KEY = api_key
        self.DJ_SSO_API_SECRET = api_secret

    @property
    def authentication_route(self):
        return f'{self.BASE_URL}/sso/web/{self.DJ_SSO_API_KEY}/'

    def get_user_details(self, token):
        url = f'{self.BASE_URL}/sso/web/{token}/verify-details'
        response = requests.get(url, headers={
            'X-ApiKey': self.DJ_SSO_API_KEY,
            'X-ApiSecret': self.DJ_SSO_API_SECRET,
        }).json()
        if response['state'] == 'VERIFIED':        # VERIFIED, EXPIRED, INCOMPLETE, INVALID
            return response['auth']






