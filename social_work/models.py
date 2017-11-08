from django.db import models

# Create your models here.
class Student(models.Model):
	name 			= 	models.CharField(max_length=300)
	reg_no          =   models.CharField(max_length=50)
	address			=	models.CharField(max_length=300)
	contact_number	=	models.IntegerField()
	email			=	models.EmailField()
	blood_group		=	models.CharField(max_length=20)
	photo			=	models.ImageField()