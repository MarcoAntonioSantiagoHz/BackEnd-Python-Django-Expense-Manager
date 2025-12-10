
# CLASS METHOD VALIDATE DATAS NO DUPLICATES

from core_api.messages import account_messages, expense_messages
from core_api.models.account import Account
from core_api.models.expense import Expense



class Validator:

    # --------------------------
    # Validation for account
    # --------------------------
   
    @staticmethod
    def account_number(data):
        if isinstance(data, list):
            data = data[0]
        account_number = data.get("account_number")
        if Account.objects.filter(account_number=account_number).exists():
            return {
                "message": account_messages.DUPLICATED_ACCOUNT_INVALID_DATA,
                # "message": account_messages.DUPLICATED_INVALID_DATA,
                "status": 400
            }
        return None

    # # --------------------------
    # # Validation for Expenses
    # # --------------------------
   

    @staticmethod
    def expense_name(data):
        if isinstance(data, list):
            data = data[0]
        name = data.get("name")
        if Expense.objects.filter(name=name).exists():
            return {
                "message": expense_messages.DUPLICATED_EXPENSE_DATA,
                "status": 400
            }
        return None
