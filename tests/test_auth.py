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



@pytest.mark.django_db
def test_login_success(api_client, create_user):
    username = "testuser"
    password = "12345678"

    create_user(username=username, password=password)

    data = {"username": username, "password": password}
    response = api_client.post("/api/login/", data, format="json")

    assert response.status_code == 200
    assert "token" in response.data



@pytest.mark.django_db
def test_login_wrong_password(api_client, create_user):
    username = "testuser"
    password = "12345678"
    wrong_password = "87654321"

    create_user(username=username, password=password)

    data = {"username": username, "password": wrong_password}
    response = api_client.post("/api/login/", data, format="json")

    assert response.status_code == 400 

    """Debería ser 401, pero por la implementación actual por defecto de DRF (obtain_auth_token) es 400. 
    REVISAR: SI SE MIGRA A JWT, CAMBIAR A 401
    """
    assert "token" not in response.data