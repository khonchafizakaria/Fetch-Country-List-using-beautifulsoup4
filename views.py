from django.shortcuts import render
from .models import Country
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import json

# Create your views here.

@csrf_exempt
def create(request):
    data = json.loads(request.body)
    print(data)
    c = Country.objects.create(name=data["name"], alpha_2=data["alpha_2"], alpha_3=data["alpha_3"], available=data["available"])
    c.save()
    return HttpResponse(status=201)
