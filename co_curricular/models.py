from django.db import models

class Image(models.Model):
	image_category       = models.CharField(max_length=100)
	description          = models.TextField()
	photo		         = models.ImageField()
	like                 = models.IntegerField(default=0)


class Events(models.Model):
	event_name       = models.CharField(max_length=100)
	event_type       = models.CharField(max_length=100)
	event_date       = models.DateTimeField()
	description      = models.TextField()
	banner_photo	 = models.ImageField()
	event_category   = models.CharField(max_length=100)
	event_schedule   = models.CharField(max_length=300)


class Archive(models.Model):
	session          =  models.CharField(max_length=20)
	archive_category =  models.CharField(max_length=100)
	photo		     =  models.ImageField()
	description      =	models.TextField()

class Cse_club(models.Model):
	club_member      = models.CharField(max_length=100)
	club_designation = models.CharField(max_length=100)
	photo 			 = models.ImageField()
	contact_number   = models.CharField(max_length=50)
	email 			 = models.EmailField()

class Game_achivement(models.Model):
	achivement_title       =  models.CharField(max_length=100)
	achivement_description =  models.TextField()
	photo		           =  models.ImageField()

class Player(models.Model):
	player_name     = models.CharField(max_length=100)
	batch           = models.PositiveIntegerField()
	player_category = models.CharField(max_length=100)
	description     = models.TextField() 
	achivement      = models.CharField(max_length=100)
	



