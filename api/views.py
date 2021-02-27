from django.shortcuts import render
from api.serializers import ExpenseSerializer, GroupSerializer
from billsplit.models import Expense, AppUser, Group
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ExpensesList(APIView):
    """
    List all expenses, or create a new expense.
    """
    def get(self, request, format=None):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response({"data": serializer.data})

    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            dict = {"data": serializer.data, "test": "test"}
            return Response(dict, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupsList(APIView):
    """
    List all groups, or create a new group.
    """
    def get(self, request, format=None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        # print(serializer.data[3])
        
        return Response({"data": serializer.data})

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            dict = {"data": serializer.data}
            return Response(dict, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)