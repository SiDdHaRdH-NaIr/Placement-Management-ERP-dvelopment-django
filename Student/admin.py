from django.contrib import admin
from .forms import DobForm
from django.utils.html import format_html
from django.core.exceptions import MultipleObjectsReturned
from .models import Student



class StudentAdminsite(admin.ModelAdmin,DobForm):
    readonly_fields=('verifyphone',)
    fieldsets =(
        ("General",{"fields":["EnquirySource"]}),
                ("Phone Verification",{"fields":("phone","verifyphone")}),
                ("Personal Information", {
                    
                "fields": [
                ("student","gender"),
                ("email","alter_email"),
                ("address","alter_address"),
                ("dob","mobile"),
                ("street","city"),
                ("state","district",),
                ("pincode","whatapp")
            ]}),
            ("Personal Information",{
                "fields":[
                    ("collagename","yearofpass"),
                    ("qualification"),
                    ("rollno","registration")
            ]}),
            ("Course info",{
                    "fields":[
                        ('course')
                ]}),(
                    ('photo'),{
                        'fields':[
                            ('photo')
                ]}),
                    ('Student Call Status',{
                        'fields':[
                            ('student_call_status'),
                            ('next_follow_up_date'),
                            ('to_staff'),
                            ("comments")
                        ]}))
    


    
    
    form=DobForm
    

    def verifyphone(self, obj):
        return format_html('<a href="#" onclick="verifyPhoneNumber()">Verify Phone Number</a>')

    verifyphone.allow_tags = True
    verifyphone.short_description = ""
    change_form_template = "student_enquiry.html"


    def save_model(self, request, obj, form, change):
            if change == False:
                # global res
                try:
                    phoneno = obj.phone
                    result = Student.objects.get(phone=phoneno)
                except Student.DoesNotExist:

                    super().save_model(request, obj, form, change)

                except MultipleObjectsReturned:
                    self.message_user(request, "Student with phone exists. Please add another.")
                except:
                    self.message_user(request, "Something went wrong")
                else:
                    self.message_user(request, "Student with phone exists. Please add another.")
            else:
                super().save_model(request, obj, form, change)



# Register your models here.
admin.site.register(Student,StudentAdminsite)



