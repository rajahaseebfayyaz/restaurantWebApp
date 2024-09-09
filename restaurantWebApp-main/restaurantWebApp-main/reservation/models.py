from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'

    def __str__(self) -> str:
        return self.user.username + ' on ' + self.date.isoformat()


class TokenModle(models.Model):
    token = models.CharField(max_length=80)
    
    class Meta:
        verbose_name = 'TokenModle'
        verbose_name_plural = 'TokenModle'

    def __str__(self) -> str:
        return self.name
