from django.contrib import admin

# Register your models here.

from django.contrib import admin
from mainapp.models import *


admin.site.register(ExpenseCategories)
admin.site.register(Expenses)
admin.site.register(IncomeCategories)
admin.site.register(Incomes)
