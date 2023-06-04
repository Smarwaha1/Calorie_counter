from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    """
    This is the model for the customer that will be visiting our website on the daily basis
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    This model will contain the choices of the meals that are avaliable to the customer
    """
    options = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.CharField(max_lenght=50, choices=options)

    def __str__(self):
        return self.name


class Fooditem(models.Model):
    """
    This model will contains the calories that is stored in each food item , that can be used in the calorie calculation
    """
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    ats = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.name


class UserFooditem(models.Model):
    """
    This model will contain the information that will be used in the user page
    """
    customer = models.ManyToManyField(Customer, blank=True)
    fooditem = models.ManyToManyField(Fooditem)









