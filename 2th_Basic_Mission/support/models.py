from operator import mod
from re import T
from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Faq(models.Model):
    question = models.TextField("Question")

    CATEGORY_CHOICES = [
        ('GENERAL','General'),
        ('ACCOUNT','Account'),
        ('ETC.','etc.'),
    ]
    category = models.CharField("CATEGORY", max_length=8, choices=CATEGORY_CHOICES, default='GENERAL')
    reply = models.TextField("REPLY")
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='FAQ_creator', verbose_name="CREATOR", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="CREATED_AT")
    updater = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='FAQ_updater', verbose_name="UPDATER", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,verbose_name="UPDATED_AT")