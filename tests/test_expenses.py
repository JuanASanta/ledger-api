import pytest
from rest_framework.authtoken.models import Token
from expenses.models import Expense

@pytest.mark.django_db
def test_create_expense(api_client, create_user):
    user = create_user(username="testuser", password="12345678") # Creamos el usuario
    token = Token.objects.create(user=user) # Creamos un token para el usuario
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}') # Autenticamos el cliente con el token
    """
    ATENCIÓN: En este caso de autenticación el token que devuelve la línea de arriba es un objeto token completo,
    lo correcto para acceder a la API es usar el token.key, que es el string del token, no el objeto completo.
    """

    data = {
        "amount": 100.0,
        "description": "Test expense",
        "date": "2023-01-01"
    }

    response = api_client.post("/api/expenses/", data, format="json")

    assert response.status_code == 201
    assert Expense.objects.filter(user=user, amount=100.0, description="Test expense").exists()