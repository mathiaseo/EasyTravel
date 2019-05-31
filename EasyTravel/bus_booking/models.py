from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_Book(models.Model):
    user_idBook = models.ForeinKey(User)
    user_mail_add = models.CharField(max_length=100)
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=32)
    user_last_name = models.CharField(max_length=32)
    user_first_name = models.CharField(max_length=32)
    user_password = models.CharField(max_length=32)

    def __str__(self):
        return self.user_idBook
    


class booking(models.Model):
    date_booking = models