from django.db import models
from django.contrib.auth.models import User

class AdvUser(models.Model):
    #is_activated = models.BooleanField(default=True) # изначально это поле содержит None
    user = models.OneToOneField(User, on_delete=models.CASCADE)

