from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Inquiry(models.Model):
    title = models.TextField('TITLE')

    CATEGORY_CHOICES = [
        ('General', 'GENERAL'),
        ('Account', 'ACCOUNT'),
        ('etc.', 'ETC.'),
    ]
    category = models.CharField('CATEGORY',max_length=10)
    email = models.TextField('E-MAIL', null=True, blank=True)
    reply_via_email = models.BooleanField('REPLY via EMAIL', default=False)
    telephone = models.TextField('TELEPHONE', null=True, blank=True)
    reply_via_MMS = models.BooleanField('REPLY via MMS', default=False)
    contents = models.TextField('CONTENTS')
    image = models.ImageField('IMAGE', null=True, blank=True)

class Answer(models.Model):
    contents = models.TextField('CONTENTS')
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Inquiry_creator', null=True)
    created_at = models.DateTimeField('CREATED_AT', auto_now_add=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Inquiry_updater', null=True)
    updated_at = models.DateTimeField('UPDATED_AT', auto_now=True)