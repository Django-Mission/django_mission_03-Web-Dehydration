# Generated by Django 4.0.4 on 2022-04-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.TextField(blank=True, null=True, verbose_name='E-MAIL'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='reply_via_MMS',
            field=models.BooleanField(default=False, verbose_name='REPLY via MMS'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='reply_via_email',
            field=models.BooleanField(default=False, verbose_name='REPLY via EMAIL'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='telephone',
            field=models.TextField(blank=True, null=True, verbose_name='TELEPHONE'),
        ),
    ]