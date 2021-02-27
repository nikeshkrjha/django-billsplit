from rest_framework import serializers
from billsplit.models import Expense, AppUser, Group
from django.contrib.auth.models import User

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'description', 'date', 'user', 'bill_image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class AppUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = AppUser
        fields = ('id', 'user', 'phone_number')

class GroupSerializer(serializers.ModelSerializer):
    members = AppUserSerializer(many=True)
    class Meta:
        model = Group
        fields = ('id','group_name', 'group_Description','members')


class AppUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = AppUser
        fields = ('id', 'user', 'phone_number')


