# Generated by Django 2.2 on 2020-12-24 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_auto_20201224_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
    ]