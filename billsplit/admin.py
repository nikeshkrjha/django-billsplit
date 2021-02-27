from django.contrib import admin

# Register your models here.
from billsplit.models import AppUser, Group, Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'date', 'user', 'bill_image')

admin.site.register(AppUser)
admin.site.register(Group)
admin.site.register(Expense, ExpenseAdmin)