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
        fields = ['id', 'amount', 'description', 'date_created',
                  'date_modified', 'user', 'bill_image', 'comments']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'password')
        # to make sure password doesn't appear on users list
        extra_kwargs = {
            'password': {'write_only': True},
        }


class AppUserSerializer(serializers.ModelSerializer):
    ''' The Serializer for AppUser Class.  '''
    user = UserSerializer()
    class Meta:
        model = AppUser
        fields = ('id', 'user', 'phone_number')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        user.set_password(user_data['password'])
        user.save()
        app_user = AppUser.objects.create(user=user, **validated_data)
        app_user.save()
        return app_user


    def update(self, instance, validated_data):
        ''' Handles update operation for users '''
        user_data = validated_data.pop('user')
        app_user = AppUser.objects.get(pk=instance.pk)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.user.last_name = user_data.get(
            'last_name', app_user.user.last_name)
        instance.user.first_name = user_data.get(
            'first_name', app_user.user.first_name)
        instance.user.email = user_data.get('email', app_user.user.email)
        instance.user.save()
        instance.save()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    members = AppUserSerializer(AppUser.objects.all, many=True)

    class Meta:
        model = Group
        fields = ('id', 'group_name', 'group_Description', 'members')

