from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Gender(models.IntegerChoices):
    MALE = 1, "male"
    FEMALE = 2, "female"
    
class Role(models.IntegerChoices):
    CHEF = 1, "chef"
    WAITER = 2, "waiter"
    SHIPPER  = 3, "shipper"

class Employee(AbstractUser):
    
    SSN = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=10, verbose_name="نام کارمند")
    last_name = models.CharField(max_length=10, verbose_name="فامیلی کارمند")
    birth_date = models.DateField()
    address = models.CharField(max_length=10, verbose_name="آدرس")
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    gender = models.IntegerField(choices=Gender.choices, verbose_name='جنسیت')
    resume = models.TextField(verbose_name="رزومه")
    bank_account_number = models.CharField(max_length=16, verbose_name="شماره کارت")
    started_at = models.DateField(auto_now_add=True)
    role = models.IntegerField(choices=Role.choices, verbose_name="نقش")
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    
    