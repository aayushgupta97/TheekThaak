
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from .views import get_extra_field

ATTRIBUTE_CHOICES = [
    ('T-Shirts',
     (
         ('Shirt Size', 'Shirt Size'),
         ('Shirt Color', 'Shirt Color'),
         ('Shirt Fabric', 'Shirt Fabric')
     )),
    ('Glasses',
     (
         ('Glass Type', 'Glass Type'),
         ('Size', 'Glass Size')
     )),
    ('Shoes',
     (
         ('Shoe Type', 'Shoe Type'),
         ('Shoe Size', 'Shoe Size')
     )),
]

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Clothing', 'Clothing'),
    ('Lifestyle', 'Lifestyle'),
)


SUB_CATEGORY_CHOICES = (
    ('T-Shirts', 'T-Shirts'),
    ('Glasses', 'Glasses'),
    ('Shoes', 'Shoes'),
)


class Customer(AbstractUser):
    gender = models.BooleanField(default=True)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        if self.first_name == '':
            return 'No Name Specified'
        else:
            return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    replacement = models.IntegerField()
    main_image = models.FileField(upload_to='product_images/', default='product_images/default.jpg')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, parent_link=True)
    image = models.FileField(upload_to='product_images/', default='product_images/default.jpg')


class ExtraAttribute(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=50)
    value = models.CharField(max_length=50)


class Attribute(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=50, choices=get_extra_field(ExtraAttribute, ATTRIBUTE_CHOICES), default='Default')
    value = models.CharField(max_length=50)
