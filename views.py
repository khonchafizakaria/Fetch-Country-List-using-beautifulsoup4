from django.shortcuts import render
from .models import Country
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# Any Request sent to a django view requires a csrf_token, we will add @csrf_exempt decorator to allow POST request.
@csrf_exempt
def create(request):
    
    # Serialize your data
    data = json.loads(request.body)
    
    # Save
    c = Country.objects.create(name=data["name"], alpha_2=data["alpha_2"], alpha_3=data["alpha_3"], available=data["available"])
    c.save()
    
    # You have to return an HttpResponse or else Django will complain. 
    return HttpResponse(status=201)
