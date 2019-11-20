from django.db import models

class TypeRequest(models.Model):
    name = models.CharField(max_length=255)
    method_name = models.CharField(max_length=256)