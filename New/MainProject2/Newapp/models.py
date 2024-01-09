from django.db import models

# Create your models here.


class CategoryDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Category image", null=True, blank=True)


class ProductDb(models.Model):
    Cat_name = models.CharField(max_length=100, null=True, blank=True)
    Pro_name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Pro_image = models.ImageField(upload_to="Product image", null=True, blank=True)
