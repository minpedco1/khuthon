from django.db import models
from django.shortcuts import get_object_or_404
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from django.contrib.auth.models import User

class ChoiceGender(models.TextChoices):
    male = '남자', '남자'
    female = '여자', '여자'
    other = '기타', '기타'

class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userID = models.CharField(max_length=20)
    gender = models.CharField(max_length=40, choices=ChoiceGender.choices)
    age = models.IntegerField(default=20)


