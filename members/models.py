from django.db import models

class Members(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length=255)
# Create your models here.
