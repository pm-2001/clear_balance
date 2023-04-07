from django.contrib import admin
from .models import Account

@admin.register(Account)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_number','balance','description']

# Register your models here.
admin.site.site_header = "Clear Balance Admin Site"