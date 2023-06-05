from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=2000)
    block = models.BooleanField(default=True)
    user_count = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    expiredAt = models.DateTimeField(null=True)


