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



@pytest.mark.django_db
def test_list_expenses(api_client, create_user, create_expense):
    user = create_user(username="testuser", password="12345678")
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    data = {
        "amount": 100.0,
        "description": "Test expense",
        "date": "2023-01-01"
    }
    data2 = {
            "amount": 30.0,
            "description": "Test expense2",
            "date": "2023-09-05"
        }
    create_expense(user=user, **data)  # Creamos un gasto existente para el usuario
    create_expense(user=user, **data2)  # Creamos un gasto existente para el usuario

    response = api_client.get("/api/expenses/")

    assert response.status_code == 200
    assert len(response.data) == 2  # Verificamos que se devuelvan los dos gastos creados
    assert Expense.objects.filter(user=user).count() == 2



@pytest.mark.django_db
def test_expense_isolation(api_client, create_user, create_expense):
    """
        Creamos un gasto para otro usuario (user2) y luego intentamos acceder a él con user1.
        Como el queryset filtra por usuario, el gasto ajeno es indistinguible de uno inexistente,
        por lo que la API debe responder 404, no 403.
    """
    data = {
            "amount": 100.0,
            "description": "Test expense",
            "date": "2023-01-01"
        }
    
    user2 = create_user(username="testuser2", email="testuser2@example.com", password="12345678")
    expense = create_expense(user=user2, **data)
    """
    En este test hay que añadir un email distinto a cada usuario porque en el modelo tiene la restricción UNIQUE,
    y al crearlo sin email, django les asigna el valor por defecto = "", que se puede comparar y falla la creación del segundo usuario,
    por haber dos email, iguales. 
    SI NECESITAMOS MAS DE UN USUARIO HAY QUE ASIGNAR UN EMAIL DISTINTO A CADA UNO, aunque no se use en el test.
    """
    user1 = create_user(username="testuser", email="testuser@example.com", password="12345678")
    token = Token.objects.create(user=user1)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    response = api_client.get(f"/api/expenses/{expense.id}/")

    assert response.status_code == 404



@pytest.mark.django_db
def test_expense_category_isolation(api_client, create_user, create_category):
    
    

    data_category = {
        "name": "Test Category",
        "color": "#FF5733"
    }
    
    
    user2 = create_user(username="testuser2", email="testuser2@example.com", password="12345678")
    category = create_category(user=user2, **data_category)
    
    
    user1 = create_user(username="testuser", email="testuser@example.com", password="12345678")
    token = Token.objects.create(user=user1)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    data_expense = {
        "amount": 100.0,
        "description": "Test expense",
        "date": "2023-01-01",
        "category": category.id  # Intentamos usar la categoría de otro usuario
    }

    response = api_client.post(f"/api/expenses/", data=data_expense)

    assert response.status_code == 400
    assert not Expense.objects.filter(description="Test expense").exists()