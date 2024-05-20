from django.contrib import admin

from audit.models import TransactionType, Transaction


# Register your models here.


class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'state', 'date_created', 'date_modified')


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
    'euser', 'transaction_type', 'source_ip', 'request_data', 'response', 'notification_response', 'successful',
    'state', 'date_created', 'date_modified')


admin.site.register(TransactionType, TransactionTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
