from django.db import models
from appadmin.models import cource

# Create your models here.

class users(models.Model):
    userid=models.AutoField(primary_key=True)
    courceid=models.ForeignKey(cource, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=500, default='', null=True)
    lastname=models.CharField(max_length=200, default='', null=True)
    username=models.CharField(max_length=200, default='', null=True)
    email=models.EmailField(max_length=200, default='', null=True)
    password=models.CharField(max_length=200, default='', null=True)
    courcenames=models.CharField(max_length=200, default='', null=True)
