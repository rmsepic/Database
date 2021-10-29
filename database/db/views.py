from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

#from models.py import MPG

class MPG(models.Model):
    id = models.AutoField(primary_key=True)
    #miles = models.FloatField()
  #  gas = models.FloatField()
   # mpg = models.FloatField()
   # location = models.CharField(max_length=100)
   # date = models.CharField(max_length=100)
   # octane = models.CharField(max_length=100)
   # price = models.CharField(max_length=100)

def index(request):
    mpg = MPG.objects.raw('SELECT miles AS id FROM gas5')
    print(mpg.model_fields)

    obj = []

    for m in mpg:
        obj.append(m.id)


    for o in obj:
        print(o)
    
    
    return render(request,"show.html",{'table':obj})
