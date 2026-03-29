from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=6, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

class Department(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=6, blank=True, null=True)
