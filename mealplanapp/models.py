from django.db import models
import datetime


# Create your models here.
class UserAccount(models.Model):
    firstName = models.CharField(max_length=2000, null=False, blank=False)
    lastName = models.CharField(max_length=2000, null=False, blank=False)
    userName = models.CharField(max_length=2000, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    mobileNumber = models.CharField(null=False, blank=False, max_length=20)

    createdOn = models.DateTimeField(default=datetime.datetime.now())
    isActive = models.BooleanField(default=True)


class MealPlan(models.Model):
    userId = models.CharField(max_length=2000, null=False, blank=False)
    mealPlanName = models.CharField(max_length=2000, null=False, blank=False)
    perDayCalories = models.CharField(max_length=2000, null=False, blank=False)
    startDate = models.DateField(null=False, blank=False)
    endDate = models.DateField(null=False, blank=False)


class EachDayMealTable(models.Model):
    userId = models.CharField(max_length=2000, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    mealName = models.CharField(max_length=2000, null=False, blank=False)
    caloriesInTaken = models.CharField(max_length=2000, null=False, blank=False)
