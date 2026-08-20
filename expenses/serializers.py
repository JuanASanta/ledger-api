from rest_framework import serializers
from .models import Category, Budget, Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'color']



class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'category', 'amount', 'period']

    def validate_category(self, value):
        request = self.context.get('request')
        if value is not None and value.user != request.user:
            raise serializers.ValidationError("Esta categoría no te pertenece.")
        return value


    
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'category', 'amount', 'description', 'date']

    def validate_category(self, value):
        request = self.context.get('request')
        if value is not None and value.user != request.user:
            raise serializers.ValidationError("Esta categoría no te pertenece.")
        return value
