from django.db import models
from django.contrib.auth.hashers import make_password
import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)

    #save customer
    def register(self):
        self.password = make_password(self.password)
        self.save()

    @staticmethod 
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return False
    
    def isExists(self):
        return Customer.objects.filter(email=self.email().exists())

    class Meta:
        verbose_name = 'Customer'

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, defaulf=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/produc')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
    
    @staticmethod 
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

