from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password

class Login(View):
    pass
