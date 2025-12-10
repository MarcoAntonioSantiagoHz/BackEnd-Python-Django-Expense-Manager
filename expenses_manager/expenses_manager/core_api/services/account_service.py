from core_api.models.account import Account
from rest_framework import status  
from core_api.serializers.account_serializer import AccountSerializer
from core_api.utils import Validator
from core_api.messages.account_messages import (
    SUCCESS_ACCOUNT_CREATED,
    SUCCESS_ACCOUNT_UPDATED,
    SUCCESS_ACCOUNT_FOUND,
    SUCCESS_ACCOUNT_DELETED,
    ERROR_ACCOUNT_NOT_FOUND,
    ERROR_ACCOUNT_INVALID_DATA,
    DUPLICATED_ACCOUNT_INVALID_DATA
)

class AccountService:

    # init first service get all accounts 
    @staticmethod
    def list_accounts():
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return serializer.data
    
    @staticmethod
    def create_account(data):
        # validate no duplicates
        error = Validator.account_number(data)
        if error:
            return error

        # Create expense if no exist duplicates
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return {
                # "message": messages["SUCCESS_CREATED"],
                "message": SUCCESS_ACCOUNT_CREATED,
                "data": serializer.data,
                "status": status.HTTP_201_CREATED
            }
        return {
            # "message": messages["ERROR_INVALID_DATA"],
            "message": ERROR_ACCOUNT_INVALID_DATA,
            "errors": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        }



    # three service put account 
    @staticmethod
    def update_account(account_id, data):
            # account = Account.objects.filter(id=account_id).first()
            account = Account.objects.get(id=account_id)
            if not account:
                return {
                    # "message": messages["ERROR_NOT_FOUND"],
                    "message": ERROR_ACCOUNT_NOT_FOUND,
                    "status": 404
                }

            serializer = AccountSerializer(account, data=data)
            if serializer.is_valid():
                serializer.save()
                return {
                    # "message": messages["SUCCESS_UPDATED"],
                    "message": SUCCESS_ACCOUNT_UPDATED,
                    "data": serializer.data,
                    "status": 200
                }
            return {
                # "message": messages["ERROR_INVALID_DATA"],
                "message": ERROR_ACCOUNT_INVALID_DATA,
                "errors": serializer.errors,
                "status": 400
            }

    # four service delete account 
    @staticmethod
    def delete_account(account_id):
        # account = Account.objects.filter(id=account_id).first()
        account = Account.objects.get(id=account_id)

        if not account:
            return {
                # "message": messages["ERROR_NOT_FOUND"],
                "message": ERROR_ACCOUNT_NOT_FOUND ,
                "status": 404
            }

        account.delete()

        return {
            # "message": messages["SUCCESS_DELETED"],
            "message": SUCCESS_ACCOUNT_DELETED,
            "status": 200
        }
    
    # five method GET ACCOUNT ONLY WITH BY ID
    @staticmethod
    def get_account_by_id(account_id):
        # account = Account.objects.filter(id=account_id).first()
        account = Account.objects.get(id=account_id)

        # if not account:
        #     return {
        #         # "message": messages["ERROR_NOT_FOUND"],
        #         "message": ERROR_ACCOUNT_NOT_FOUND,
        #         "status": 404
        #     }
        try:
             account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
             return {
                  "message": ERROR_ACCOUNT_NOT_FOUND,
                  "status": 404
            }

        serializer = AccountSerializer(account)

        return {
            # "message": messages["SUCCESS_FOUND"],
            "message": SUCCESS_ACCOUNT_FOUND,
            "data": serializer.data,
            "status": 200
        }

