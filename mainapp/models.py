from django.db import models

# Create your models here.

from django.db import models


class ExpenseCategories(models.Model):
    category = models.CharField(max_length=25, null=False)


class Expenses(models.Model):
    ammount = models.FloatField(null=False)
    expense_category = models.ForeignKey(ExpenseCategories, null=False, on_delete=models.PROTECT)


class IncomeCategories(models.Model):
    category = models.CharField(max_length=25, null=False)


class Incomes(models.Model):
    ammount = models.FloatField(null=False)
    income_category = models.ForeignKey(IncomeCategories, null=False, on_delete=models.PROTECT)




