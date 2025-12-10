# For the modelviewset, we need a DRG that
#  handles the default route to support CRUD.

from rest_framework.routers import DefaultRouter

from core_api.views.account_views import AccountViewSet
from core_api.views.expense_views import ExpenseViewSet


# declare registers only router for endpoints
router = DefaultRouter()
router.register('accounts', AccountViewSet, basename='account')
router.register('expenses', ExpenseViewSet, basename='expense')
router.register('payments', ExpenseViewSet, basename='payment')
urlpatterns = router.urls