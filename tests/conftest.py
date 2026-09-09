import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

@pytest.fixture
def create_user(db):
    user_model = get_user_model()

    def make_user(**kwargs):
        return user_model.objects.create_user(**kwargs)
    
    return make_user

@pytest.fixture
def api_client():
    return APIClient()