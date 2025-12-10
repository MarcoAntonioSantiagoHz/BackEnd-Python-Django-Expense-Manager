# We create the controllers, 
# we need "modeViewSet"  class of Django's to create the HTTP verbs


from rest_framework.decorators import api_view

from core_api import messages
from core_api.services.expense_service import ExpenseService
from rest_framework.response import Response


@api_view(['GET']) # method declare for get all expenses
def get_expenses(request):
    data = ExpenseService.list_expenses()
    return Response(data)

@api_view(['GET']) # method declare for get only by id expense
def get_expense_by_id(request, expense_id):
    result = ExpenseService.get_expense_by_id(expense_id)
    return Response(result, status=result["status"])



@api_view(['POST'])
def create_expense(request): # method declare for create expense
    result = ExpenseService.create_expense(request.data)
    return Response(result, status=result["status"])

# method update only status
@api_view(['PATCH'])
def patch_expense_status(request, expense_id):
    new_status = request.data.get("status")
    if not new_status:
        return Response({
            "message": messages.expense_messages.ERROR_INVALID_DATA_EXPENSE
        }, status=400)

    result = ExpenseService.update_expense_status(expense_id, new_status)
    return Response(result, status=result["status"])

# method update all expenses

@api_view(['PUT'])
def update_expense(request, expense_id): # method declare for update only by id expense
    # get the expense_id from the URL.
    result = ExpenseService.update_expense(expense_id, request.data)
    return Response(result, status=result["status"])