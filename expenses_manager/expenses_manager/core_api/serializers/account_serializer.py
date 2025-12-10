
# serializer convert object model to format json api

# from rest_framework import serializers  
# from core_api import serializers
# from core_api.models.account import Account # The import requires a template that we will use.
from rest_framework import serializers
from core_api.models.account import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta: # We tell it to serialize only the fields of the account model.
        model = Account
        fields = '__all__'