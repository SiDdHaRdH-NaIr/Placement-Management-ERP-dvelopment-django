from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Student
from django.core.exceptions import MultipleObjectsReturned
import json


# Create your views here.
def verifyphone(request):
    global res
    try:
        id=request.GET.get('id',)
        student= Student.objects.get(phone=id)
    


    except Student.DoesNotExist:
        res ={'message': "Phone does not exist. Proceed"} 
    except:
        res= {"message": "Something went wrong"}
    else:
        res= {"message": "Student with phone exists. Please add another."}
    return HttpResponse(json.dumps(res), content_type="application/json")


