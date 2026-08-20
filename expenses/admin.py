from django.contrib import admin
from .models import Category, Expense, Budget

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'color')
    search_fields = ('name', 'user__username')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'date')
    search_fields = ('description', 'category__name', 'date')

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'period')
    search_fields = ('category__name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Budget, BudgetAdmin)