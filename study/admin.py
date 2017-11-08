from django.contrib import admin
from .models import Merit
from .models import Teacher

class meritlist(admin.ModelAdmin):
	list_display = ['session','student_name']
class Tracherlist(admin.ModelAdmin):
	list_display = ['name','contact_number','photo']

admin.site.register(Merit,meritlist)
admin.site.register(Teacher,Tracherlist)