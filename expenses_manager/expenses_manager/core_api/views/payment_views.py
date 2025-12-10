# We create the controllers, 
# we need "modeViewSet"  class of Django's to create the HTTP verbs


from core_api import messages
from core_api.messages.payment_messages import ERROR_PAYMENT_INVALID_DATA
from core_api.services.payment_service import PaymentService
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET']) # method declare for get all payments
def get_payments(request):
    data = PaymentService.list_payments()
    return Response(data)

@api_view(['GET']) # method declare for get only by id payments
def get_payment_by_id(request, payment_id):
    result = PaymentService.get_payment_by_id(payment_id)
    return Response(result, status=result["status"])



@api_view(['POST'])
def create_payment(request): # method declare for create payments
    result = PaymentService.create_payment(request.data)
    return Response(result, status=result["status"])


# method update only status
@api_view(['PATCH'])
def patch_payment_status(request, payment_id):
    new_status = request.data.get("status")
    if not new_status:
        return Response({
            "message": ERROR_PAYMENT_INVALID_DATA
        }, status=400)

    result = PaymentService.update_payment_status(payment_id, new_status)
    return Response(result, status=result["status"])



# method update all payments

@api_view(['PUT'])
def update_payment(request, payment_id): # method declare for update only by id expense
    # get the payment_id from the URL.
    result = PaymentService.update_payment(payment_id, request.data)
    return Response(result, status=result["status"])