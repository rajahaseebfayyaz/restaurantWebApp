from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=30)