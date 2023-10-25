from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


def get_or_create_user(auth):
    features = auth['features']
    username = features['username']
    User = get_user_model()
    try:
        user = User.objects.get(username=username)      # raise
    except ObjectDoesNotExist:
        registration_features = ('username', 'email', 'first_name', 'last_name')
        user = User.objects.create_user({key: auth[key] for key in auth if key in registration_features})         # raise
    return user