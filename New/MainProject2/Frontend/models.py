from django.db import models

# Create your models here.


class ContactDb(models.Model):
    Firstname = models.CharField(max_length=20, null=True, blank=True)
    Lastname = models.CharField(max_length=20, null=True, blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=20, null=True, blank=True)
    Telephone = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)


class UserRegDb(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    pass_word = models.CharField(max_length=20, null=True, blank=True)
    Mob_number = models.IntegerField(null=True, blank=True)


class CartDB(models.Model):
    Username = models.CharField(max_length=30, null=True, blank=True)
    Prod_name = models.CharField(max_length=50, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Total_price = models.IntegerField(null=True, blank=True)
    Description = models.CharField( max_length=100, null=True, blank=True)


class OrderDb(models.Model):
    First_name = models.CharField(max_length=20, null=True, blank=True)
    Last_name = models.CharField(max_length=20, null=True, blank=True)
    E_mail = models.EmailField(max_length=20, null=True, blank=True)
    A_dress = models.TextField(max_length=100, null=True, blank=True)
    C_ity = models.CharField(max_length=20, null=True, blank=True)
    Country = models.CharField(max_length=20, null=True, blank=True)
    Zipcode = models.CharField(max_length=20, null=True, blank=True)
    Tele = models.IntegerField(null=True, blank=True)
