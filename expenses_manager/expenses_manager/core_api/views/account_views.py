# We create the controllers, 
# we need "modeViewSet"  class of Django's to create the HTTP verbs


# from rest_framework import viewsets
# from core_api.models.account import Account
# from core_api.serializers.account_serializer import AccountSerializer

# class AccountViewSet(viewsets.ModelViewSet):
#     queryset = Account.objects.all() # Data set that we are going to use the Django ORM for.
#     serializer_class = AccountSerializer



















# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from core_api.models import Account
# from core_api.messages.account_messages import messages
# from core_api.serializers.account_serializer import AccountSerializer
# from core_api.services.account_service import AccountService

# @api_view(['GET'])
# # def get_accounts(request):
# def get_accounts(request):
#     accounts = Account.objects.all()
#     serializer = AccountSerializer(accounts, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_account(request):
#     serializer = AccountSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         # return Response(serializer.data, status=status.SUCCESS_CREATED)
#         return Response(
#             {"message": messages["SUCCESS_CREATED"], "data": serializer.data},
#             status=status.HTTP_201_CREATED
#         )
#     return Response(
#         {"message": messages["ERROR_INVALID_DATA"], "errors": serializer.errors},
#         status=status.HTTP_400_BAD_REQUEST
#     )


# --------------------------------------------------------------------

# VERSION2


from rest_framework.decorators import api_view
from rest_framework.response import Response
from core_api.services.account_service import AccountService


@api_view(['GET']) # method declare for get all accounts
def get_accounts(request):
    data = AccountService.list_accounts()
    return Response(data)

@api_view(['GET']) # method declare for get only by id account
def get_account_by_id(request, account_id):
    result = AccountService.get_account_by_id(account_id)
    return Response(result, status=result["status"])



@api_view(['POST'])
def create_account(request): # method declare for create account
    result = AccountService.create_account(request.data)
    return Response(result, status=result["status"])


@api_view(['PUT'])
def update_account(request, account_id): # method declare for update only by id account
    # result = AccountService.update_account(request.data)
    # return Response(result, status=result["status"])
    # get the account_id from the URL.
    result = AccountService.update_account(account_id, request.data)
    return Response(result, status=result["status"])

@api_view(['DELETE']) # method declare for delete  account by id
def delete_account(request, account_id):
    data = AccountService.delete_account(account_id)
    return Response(data, status=data["status"])


