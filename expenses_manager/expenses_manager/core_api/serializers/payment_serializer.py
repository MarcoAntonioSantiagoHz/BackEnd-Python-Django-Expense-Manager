
# serializer convert object model to format json api

from rest_framework import serializers
from core_api.models.payment import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta: # We tell it to serialize only the fields of the account model.
        model = Payment # serializer model to object json
        fields = '__all__'