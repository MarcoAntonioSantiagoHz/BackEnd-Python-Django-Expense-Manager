
# from core_api.constants import status
from rest_framework import status
from core_api.messages.expense_messages import (
    SUCCESS_CREATED_EXPENSE,
    SUCCESS_FOUND_EXPENSE,
    SUCCESS_UPDATED_EXPENSE,
    # SUCCESS_DELETED_EXPENSE,
    ERROR_NOT_FOUND_EXPENSE,
    ERROR_INVALID_DATA_EXPENSE
)





from core_api.models.expense import Expense
from core_api.serializers.expense_serializer import ExpenseSerializer
from core_api.utils import Validator


class ExpenseService:

    # Obtener todos los expenses
    @staticmethod
    def list_expenses():
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return serializer.data

    # Obtener un expense por ID
    @staticmethod
    def get_expense_by_id(expense_id):
        try:
            expense = Expense.objects.get(id=expense_id)
        except Expense.DoesNotExist:
            return {
                "message": ERROR_NOT_FOUND_EXPENSE,
                "status": 404,
            }

        serializer = ExpenseSerializer(expense)
        return {
            "message": SUCCESS_FOUND_EXPENSE,
            "data": serializer.data,
            "status": 200,
        }

    # Crear un expense sin duplicados
    @staticmethod
    def create_expense(data):
        # Validar duplicado
        error = Validator.expense_name(data)
        if error:
            return error

        # Crear expense si no existen duplicados
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return {
                "message": SUCCESS_CREATED_EXPENSE,
                "data": serializer.data,
                "status": status.HTTP_201_CREATED
            }

        return {
            "message": ERROR_INVALID_DATA_EXPENSE,
            "errors": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        }

    # update only status for expense
    @staticmethod
    def update_expense_status(expense_id, new_status):
        try:
            expense = Expense.objects.get(id=expense_id)
        except Expense.DoesNotExist:
            return {
                "message": ERROR_NOT_FOUND_EXPENSE,
                "status": 404
            }

        serializer = ExpenseSerializer(expense, data={"status": new_status}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return {
                "message": SUCCESS_UPDATED_EXPENSE,
                "data": serializer.data,
                "status": 200
            }

        return {
            "message": ERROR_INVALID_DATA_EXPENSE,
            "errors": serializer.errors,
            "status": 400
        }

    # update all expense
    @staticmethod
    def update_expense(expense_id, data):
            # expense = Expense is model
            expense = Expense.objects.get(id=expense_id)
            if not expense:
                return {
                    "message":ERROR_NOT_FOUND_EXPENSE,
                    "status": 404
                }

            serializer = ExpenseSerializer(expense, data=data)
            if serializer.is_valid():
                serializer.save()
                return {
                    "message": SUCCESS_UPDATED_EXPENSE,
                    "data": serializer.data,
                    "status": 200
                }
            return {
                "message": ERROR_INVALID_DATA_EXPENSE,
                "errors": serializer.errors,
                "status": 400
            }
