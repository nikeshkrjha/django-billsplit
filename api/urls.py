from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.ExpensesList.as_view(), name='expenses-list'),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view(),name='expense-item'),
    path('groups/', views.GroupsList.as_view(), name='groups-list'),
    path('comments/', views.ExpenseCommentList.as_view(), name='exp-cmt-list'),
    path('comments/<int:pk>/', views.ExpenseCommentDetail.as_view(), name='comment-item')
]