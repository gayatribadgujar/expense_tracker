from django.urls import path
from .views import signup_view, expense_list, add_expense,delete_expense

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
]