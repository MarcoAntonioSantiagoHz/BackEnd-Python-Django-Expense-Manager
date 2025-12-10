
# serializer convert object model to format json api

# from rest_framework import serializers 

# # from core_api import serializers
# from core_api.models.expense import Expense # The import requires a template that we will use.
from rest_framework import serializers
from core_api.models.expense import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta: # We tell it to serialize only the fields of the "expense" model.
        model = Expense
        fields = '__all__'