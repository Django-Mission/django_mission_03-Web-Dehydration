# Generated by Django 4.0.4 on 2022-05-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='category',
            field=models.CharField(choices=[('General', 'GENERAL'), ('Account', 'ACCOUNT'), ('etc.', 'ETC.')], default='GENERAL', max_length=10, verbose_name='CATEGORY'),
        ),
    ]
