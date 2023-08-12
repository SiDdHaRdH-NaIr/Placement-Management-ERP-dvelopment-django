from django.db import models
from Employee_app.models import State,District,EnquirySource,Qualification,Followupstatusname,Course
from smart_selects.db_fields import ChainedForeignKey
from django.contrib import messages
from django.forms import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")

    

# Create your models here.





class Student(models.Model):
    
    PLATFORM_CHOICES1 = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )

    import datetime
    YEAR_CHOICES = []
    for r in range((datetime.datetime.now().year - 15), (datetime.datetime.now().year + 5)):
        YEAR_CHOICES.append((r, r))
    

    


    
    EnquirySource=models.ForeignKey(EnquirySource,on_delete=models.CASCADE)

                
    phone = models.CharField(max_length=10, verbose_name='Phone')
    



    student = models.CharField(max_length=255, verbose_name="Student:")
    gender= models.CharField(max_length=20, choices=PLATFORM_CHOICES1, verbose_name="Gender:")
    email = models.EmailField(verbose_name="Email:")
    alter_email=models.EmailField(verbose_name="Alternative Email:", blank=True)
    address =models.CharField(max_length=255, verbose_name="Address:", blank=True)
    alter_address =models.CharField(max_length=255, verbose_name="Alternative Address:", blank=True)
    dob=models.DateField(verbose_name="Dop:")
    mobile=models.CharField(max_length=10, verbose_name="Mobile:", blank=True, validators=[phone_regex])
    street=models.CharField(max_length=255, verbose_name="Street:", blank=True)
    city =models.CharField(max_length=255, blank=True, verbose_name="City:")
    state =models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="State:")
    district =ChainedForeignKey(District,chained_field="state",chained_model_field="state",show_all=False,auto_choose=True,sort=True, verbose_name="District:")

    pincode=models.CharField(max_length=6, verbose_name="Pincode:",blank=True)
    whatapp=models.CharField(max_length=10, verbose_name="Whatsapp:")



    #acdamic info
    collagename=models.CharField(max_length=255,verbose_name='Collage Name:')
    qualification=models.ForeignKey(Qualification,on_delete=models.CASCADE,verbose_name='Qualification Name')
    yearofpass=models.PositiveIntegerField(choices=YEAR_CHOICES, blank=False, null=False, verbose_name="Year of Pass")
    rollno=models.CharField(max_length=255,verbose_name="Roll No")
    registration=models.CharField(max_length=255, verbose_name="Registration Number:")

    #courseinfo
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    #Photo
    photo=models.ImageField(upload_to='photo_student')


    #student call status
    student_call_status=models.ForeignKey(Followupstatusname,on_delete=models.CASCADE,verbose_name="Student Call Status")
    next_follow_up_date=models.DateField(null=True,verbose_name="Next Follow-up Date:")
    to_staff=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='To Staff')
    comments=models.CharField(max_length=255,verbose_name='Comments:')
