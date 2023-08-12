from django.contrib import admin
from .models import Company,State,District,Qualification,Branch,EnquirySource,Course,Followupstatusname,MasterData,Batch
from .forms import BachForm 
from django.contrib.admin import AdminSite


class BatchAdmin(admin.ModelAdmin):
    list_display=('course','trainer','start_date','end_date')
    form=BachForm


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal=('trainers',)           
        

admin.site.register(District, order=1)
admin.site.register(State)
admin.site.register(Qualification)
admin.site.register(Branch)
admin.site.register(Batch,BatchAdmin)
admin.site.register(EnquirySource)
admin.site.register(Company)
admin.site.register(Course,CourseAdmin)
admin.site.register(Followupstatusname)
admin.site.register(MasterData)



