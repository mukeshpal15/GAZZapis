from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser


# Create your models here.
class user(models.Model):
	id = models.AutoField(primary_key=True)
	username=models.CharField(max_length=50)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	phone_no=models.CharField(max_length=15)

	

class useres(models.Model):
	Nickname=models.CharField(max_length=50, blank=True)
	Full_Name=models.CharField(max_length=50)
	email=models.CharField(max_length=50, primary_key=True)
	phone_no=models.CharField(max_length=15, blank=True)
	password=models.CharField(max_length=70)
	img = models.ImageField(upload_to='user_pic', default='user_pic/icon.png')
	Description=models.TextField(blank = True, default='Add Your Description')
	Social_link=models.CharField(max_length=300 ,blank=True)


	class Meta:
		db_table="useres"
