from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    about = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    photo = models.ImageField(upload_to='posts/%Y/%m/%d/')
