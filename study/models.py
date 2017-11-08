from django.db import models

class Merit(models.Model):
	session       = models.CharField(max_length=100)
	level  		  = models.CharField(max_length=20)
	student_name  = models.CharField(max_length=100)
	cgpa 		  = models.FloatField()
	position  	  = models.PositiveIntegerField()


class Teacher(models.Model):
	name 			= 	models.CharField(max_length=300)
	designation		=	models.CharField(max_length=300)
	address			=	models.CharField(max_length=300)
	contact_number	=	models.IntegerField()
	email			=	models.EmailField()
	blood_group		=	models.CharField(max_length=20)
	photo			=	models.ImageField()
	