from turtle import mode
from django.db import models

# Create your models here.
class platform(models.Model):
    platformid=models.AutoField(primary_key=True)
    platformname=models.CharField(max_length=255, default='', null=True)
    platformdsp=models.CharField(max_length=2055, default='', null=True)

class cource(models.Model):
    courceid=models.AutoField(primary_key=True)
    platformid=models.ForeignKey(platform, on_delete=models.CASCADE)
    courcenames=models.CharField(max_length=200, default='', null=True)
    coursedsp=models.CharField(max_length=200, default='', null=True)
    coursemodules=models.CharField(max_length=200, default='', null=True)
    courselevel=models.CharField(max_length=200, default='', null=True)

class tutorial(models.Model):
    tutorialid=models.AutoField(primary_key=True)
    courceid=models.ForeignKey(cource, on_delete=models.CASCADE)
    vedioname=models.CharField(max_length=200, default='', null=True)
    vediodsp=models.CharField(max_length=2000, default='', null=True)
    vedio=models.FileField(default='vedio.mp4', upload_to='vedio')

class questions(models.Model):
    questionsid=models.AutoField(primary_key=True)
    tutorialid=models.ForeignKey(tutorial, on_delete=models.CASCADE)
    courceid=models.ForeignKey(cource, on_delete=models.CASCADE)
    question=models.CharField(max_length=500, default='', null=True)
    option1=models.CharField(max_length=200, default='', null=True)
    option2=models.CharField(max_length=200, default='', null=True)
    option3=models.CharField(max_length=200, default='', null=True)
    answers=models.CharField(max_length=200, default='', null=True)