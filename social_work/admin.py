from django.contrib import admin
from .models import Student
class Studentlist(admin.ModelAdmin):
	list_display = ['name','contact_number','photo']

admin.site.register(Student,Studentlist)