from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Accounts
from .models import Payments


admin.site.register(Accounts)
admin.site.register(Payments)

