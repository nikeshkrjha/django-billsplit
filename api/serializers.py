from rest_framework import serializers
from billsplit.models import Expense, AppUser, Group, ExpenseComment
from django.contrib.auth.models import User

class ExpenseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseComment
        fields = ('__all__')


class ExpenseSerializer(serializers.ModelSerializer):
    comments = ExpenseCommentSerializer(many=True)
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'description', 'date_created', 'date_modified', 'user', 'bill_image','comments']

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



