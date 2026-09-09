import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_register_user(api_client):
    data = {
    "username": "testuser",
    "email": "test@example.com",
    "name": "Test User",
    "password": "12345678"
    }

    response = api_client.post("/api/register/", data, format="json")

    assert response.status_code == 201
    assert get_user_model().objects.filter(username="testuser").exists()
    