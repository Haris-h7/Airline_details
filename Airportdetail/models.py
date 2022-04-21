from django.db import models

# Create your models here.
class Data(models.Model):
    jsonfile = models.FileField(upload_to="file", null=True, blank=True)