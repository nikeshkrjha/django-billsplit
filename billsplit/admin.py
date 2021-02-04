from django.contrib import admin

# Register your models here.
from billsplit.models import AppUser, Group, Expense

admin.site.register(AppUser)
admin.site.register(Group)
admin.site.register(Expense)