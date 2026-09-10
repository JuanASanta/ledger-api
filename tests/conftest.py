import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from expenses.models import Expense, Category



@pytest.fixture
def create_user(db):
    user_model = get_user_model()

    def make_user(**kwargs):
        return user_model.objects.create_user(**kwargs)
    
    return make_user



@pytest.fixture
def api_client():
    return APIClient()



@pytest.fixture
def create_expense(db):

    def make_expense(user, **kwargs):
        return Expense.objects.create(user=user, **kwargs)
    
    return make_expense



@pytest.fixture
def create_category(db):

    def make_category(user, **kwargs):
        return Category.objects.create(user=user, **kwargs)
    
    return make_category