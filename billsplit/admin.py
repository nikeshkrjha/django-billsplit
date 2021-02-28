from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from billsplit.models import AppUser, Group, Expense, ExpenseComment

# ModelAdmin classes for all the models
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'date_created', 'date_modified', 'user', 'bill_image')


class AppUserAdmin(admin.ModelAdmin):
    # class Meta:
    #     model
    list_display = ('user','phone_number')
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_Description')

class ExpenseCommentAdmin(admin.ModelAdmin):
    list_display = ('comment','expense_item','commented_by','date_modified')

# Registering models to make the available on the admin site
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseComment, ExpenseCommentAdmin)
