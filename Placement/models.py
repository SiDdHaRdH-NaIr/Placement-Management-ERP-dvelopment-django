from django.db import models
from Employee_app.models import Course



class Job_title(models.Model):
    Job_title=models.CharField(max_length=200)
# Create your models here.
class Employeer(models.Model):
    gender=(('male',"Male"),('female',"Female"),('others','Others'),)


    company_name=models.CharField(max_length=200)
    no_of_vacancy=models.CharField(max_length=100)
    job_location=models.CharField(max_length=200)
    Gender=models.CharField(max_length=20,choices=gender)
    description=models.TextField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    job_title=models.ForeignKey(Job_title,on_delete=models.CASCADE)
    salary=models.CharField(max_length=6)
    last_date=models.DateField()
