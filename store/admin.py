from django.contrib import admin
from .models import Products, Customer, Category, Orders 

# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    # This shows these specific columns in the admin list
    list_display = ('name', 'price', 'stock', 'category')
    
    # This adds a search bar to find products quickly
    search_fields = ('name',)
    
    # This adds a filter sidebar on the right
    list_filter = ('category',)

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered')
    readonly_fields = ('date_ordered',) # Prevents changing the date manually

admin.site.register(Customer)
admin.site.register(Category)

