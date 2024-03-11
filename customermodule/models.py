from django.db import models
from django.shortcuts import render
# Create your models here.
def viewfood(request):
    return render(request,'customermodule/viewfood.html')

