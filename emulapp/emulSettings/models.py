from django.db import models
from django.utils.translation import gettext_lazy as _

class TypeRequest(models.Model):

    class rqFormatTypes(models.TextChoices):
        XML = 'xml'
        JSON = 'json'

    type_name = models.CharField(max_length=255)
    format_type = models.CharField(max_length=255, choices= rqFormatTypes.choices, default='XML')
    method_name = models.CharField(max_length=255)  


class ObjectModel(models.Model):
    responseText = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    typeRequst = models.ForeignKey(TypeRequest,on_delete=models.CASCADE)


class SearchRules(models.Model):
    xpath = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    objectModel = models.ForeignKey(ObjectModel, on_delete=models.CASCADE)