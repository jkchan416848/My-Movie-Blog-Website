from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class RegisterModel(User):
    Phone_no = models.PositiveBigIntegerField()
