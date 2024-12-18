from django.contrib import admin
from .models import User, Stock, Account, Achievement, Transaction


admin.site.register(User)
admin.site.register(Stock)
admin.site.register(Account)
admin.site.register(Achievement)
admin.site.register(Transaction)