from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Expense(models.Model):
    amount = models.DecimalField(verbose_name='Amount', max_digits=11,decimal_places=2,null=False)
    description = models.TextField(verbose_name='Details', max_length=200)
    date = models.DateTimeField(verbose_name='Date', default=timezone.now)
    user = models.ForeignKey('AppUser', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.date + "-" + self.amount
    

class Group(models.Model):
    group_name = models.CharField(max_length=25, verbose_name='Group Name', blank=False)
    group_Description = models.TextField(verbose_name='Details', max_length=200)
    members = models.ManyToManyField('AppUser', verbose_name=("members"), null=True)

    def __str__(self):
        return self.group_name

# The AppUser model. Represents a user of the app.
class AppUser(models.Model):
    user = models.OneToOneField(User, related_name='app_user',on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            AppUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.app_user.save()
