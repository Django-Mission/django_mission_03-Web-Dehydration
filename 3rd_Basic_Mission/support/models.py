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
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='FAQ_created_by', verbose_name="CREATOR", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="CREATED_AT")
    updater = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='FAQ_updated_by', verbose_name="UPDATER", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,verbose_name="UPDATED_AT")

class Inquiry(models.Model):
    title = models.TextField('TITLE')

    CATEGORY_CHOICES = [
        ('General', 'GENERAL'),
        ('Account', 'ACCOUNT'),
        ('etc.', 'ETC.'),
    ]
    category = models.CharField('CATEGORY', max_length=10, choices=CATEGORY_CHOICES, default='GENERAL')
    email = models.TextField('E-MAIL', null=True, blank=True)
    reply_via_email = models.BooleanField('REPLY via EMAIL', default=False)
    telephone = models.TextField('TELEPHONE', null=True, blank=True)
    reply_via_MMS = models.BooleanField('REPLY via MMS', default=False)
    contents = models.TextField('CONTENTS')
    image = models.ImageField('IMAGE', null=True, blank=True)
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='Inquiry_created', verbose_name="CREATOR", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="CREATED_AT")
    
    STATUS_CHOICES = [
        ('Inquiry Registered', '문의 등록'),
        ('Inquiry Received', '접수 완료'),
        ('Answer Completed', '답변 완료'),
    ]
    status = models.CharField('STATUS', max_length=20, choices=STATUS_CHOICES, default='Inquiry Registered')

class Answer(models.Model):
    contents = models.TextField('CONTENTS', null=True, blank=True)
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Answer_created', null=True, blank=True)
    created_at = models.DateTimeField('CREATED_AT', auto_now_add=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Answer_updated', null=True, blank=True)
    updated_at = models.DateTimeField('UPDATED_AT', auto_now=True)