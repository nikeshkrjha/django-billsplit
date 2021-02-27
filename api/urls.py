from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.ExpensesList.as_view(), name='expenses-list'),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view()),
    path('groups/', views.GroupsList.as_view(), name='groups-list')
]