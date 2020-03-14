from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils import timezone
import django

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)	
	Matriculation_Number = models.CharField(max_length=20, unique=True)
	department = models.CharField(max_length=60)
	Faculty = models.CharField(max_length=50)
	Level = models.CharField(max_length=12)	
	password = models.CharField(max_length=200)
	def __str__(self):
		return self.Matriculation_Number
class It(models.Model):
	full_name = models.CharField(max_length=500)	
	Matriculation_Number = models.CharField(max_length=20, unique=True)
	course_of_study = models.CharField(max_length=60)
	Faculty = models.CharField(max_length=50)
	Level = models.CharField(max_length=12)	
	name_of_the_company = models.CharField(max_length=500)
	address_of_the_company = models.CharField(max_length=500)
	department = models.CharField(max_length=200)
	name_of_industry_based_supervisor = models.CharField(max_length=500)
	address_of_industry_based_supervisor = models.CharField(max_length=500)
	def __str__(self):
		return self.Matriculation_Number






