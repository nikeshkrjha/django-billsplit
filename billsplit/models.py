from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Expense(models.Model):
    """ The Expense model - represents the expense item """
    amount = models.DecimalField(verbose_name='Amount', max_digits=11,decimal_places=2,null=False)
    description = models.TextField(verbose_name='Details', max_length=200)
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True, null=True)
    date_modified = models.DateTimeField(verbose_name='Date Modified', auto_now=True, null=True)
    user = models.ForeignKey('AppUser', on_delete=models.CASCADE, null=False)
    bill_image = models.ImageField(default="", upload_to='images', null=True)

    def __str__(self):
        return self.description + "-" + str(self.date_created) + "- $" + str(self.amount)


class ExpenseComment(models.Model):
    """ The ExpenseComments model - represents the comment made about an expense item """
    comment = models.TextField(verbose_name='Comment', max_length=200)
    expense_item = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True, related_name='comments')
    commented_by = models.ForeignKey('AppUser', on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True, null=True)
    date_modified = models.DateTimeField(verbose_name='Date Modified', auto_now=True, null=True)
    

class Group(models.Model):
    """ The Group model - represents the groups a user has created or is a member of """
    group_name = models.CharField(max_length=25, verbose_name='Group Name', blank=False)
    group_Description = models.TextField(verbose_name='Details', max_length=200)
    members = models.ManyToManyField('AppUser', verbose_name=("members"))

    def __str__(self):
        return self.group_name

# The AppUser model. Represents a user of the app.
class AppUser(models.Model):
    """ The AppUser model - represents the user of the app """
    user = models.OneToOneField(User, related_name='app_user',on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username
    
    #create user instance upon save of AppUser object and assign it to the user property
    # @receiver(post_save, sender=User)
    # def create_user_profile(self, sender, instance, created, **kwargs):
    #     if created:
    #         AppUser.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(self, sender, instance, **kwargs):
    #     instance.app_user.save()
