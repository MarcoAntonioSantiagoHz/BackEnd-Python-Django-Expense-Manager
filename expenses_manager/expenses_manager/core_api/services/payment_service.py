
from core_api.messages.payment_messages import (
    ERROR_PAYMENT_INVALID_DATA,
    ERROR_PAYMENT_NOT_FOUND,
    SUCCESS_CREATED_PAYMENT,
    SUCCESS_FOUND_PAYMENT,
    SUCCESS_UPDATED_PAYMENT,
)
from core_api.models.payment import Payment
from core_api.serializers.payment_serializer import PaymentSerializer
from rest_framework import status


class PaymentService:

    # LIST ALL PAYMENTS
    @staticmethod
    def list_payments():
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return serializer.data

    # GET PAYMENT BY ID
    @staticmethod
    def get_payment_by_id(payment_id):
        try:
            payment = Payment.objects.get(id=payment_id)
        except Payment.DoesNotExist:
            return {
                "message": ERROR_PAYMENT_NOT_FOUND,
                "status": 404
            }

        serializer = PaymentSerializer(payment)
        return {
            "message": SUCCESS_FOUND_PAYMENT,
            "data": serializer.data,
            "status": 200
        }

    # CREATE PAYMENT
    @staticmethod
    def create_payment(data):
        serializer = PaymentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return {
                "message": SUCCESS_CREATED_PAYMENT,
                "data": serializer.data,
                "status": status.HTTP_201_CREATED
            }

        return {
            "message": ERROR_PAYMENT_INVALID_DATA,
            "errors": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        }

    # PATCH ONLY STATUS
    @staticmethod
    def update_payment_status(payment_id, new_status):
        try:
            payment = Payment.objects.get(id=payment_id)
        except Payment.DoesNotExist:
            return {
                "message": ERROR_PAYMENT_NOT_FOUND,
                "status": 404
            }

        serializer = PaymentSerializer(payment, data={"status": new_status}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return {
                "message": SUCCESS_UPDATED_PAYMENT,
                "data": serializer.data,
                "status": 200
            }

        return {
            "message": ERROR_PAYMENT_INVALID_DATA,
            "errors": serializer.errors,
            "status": 400
        }

        # UPDATE ALL PAYMENT
    @staticmethod
    def update_payment(payment_id, data):
            # payment = Payment is model
            payment = Payment.objects.get(id=payment_id)
            if not payment:
                return {
                    "message":ERROR_PAYMENT_NOT_FOUND,
                    "status": 404
                }

            serializer = PaymentSerializer(payment, data=data)
            if serializer.is_valid():
                serializer.save()
                return {
                    "message": SUCCESS_UPDATED_PAYMENT,
                    "data": serializer.data,
                    "status": 200
                }
            return {
                "message": ERROR_PAYMENT_INVALID_DATA,
                "errors": serializer.errors,
                "status": 400
            }