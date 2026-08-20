from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BudgetViewSet, ExpenseViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('budgets', BudgetViewSet, basename='budget')
router.register('expenses', ExpenseViewSet, basename='expense')

urlpatterns = router.urls