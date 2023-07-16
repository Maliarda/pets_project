# import os
#
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pets_project.settings")
# import django
#
#
# django.setup()
import pytest
from django.test import Client
from rest_framework_simplejwt.tokens import AccessToken

from pets.models import User


@pytest.fixture
def api_client():
    return Client()


@pytest.fixture
def user():
    return User.objects.create_user(
        username="testuser", password="testpassword"
    )


@pytest.fixture
def auth_token(user):
    token = AccessToken.for_user(user)
    return token


@pytest.fixture
def auth_api_client(api_client, auth_token):
    api_client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {str(auth_token)}"
    return api_client
