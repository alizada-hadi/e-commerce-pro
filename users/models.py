from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="users/profile", default="user.jpg")
    address = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.first_name
