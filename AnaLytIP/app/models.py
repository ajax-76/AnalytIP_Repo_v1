"""
Definition of models.
"""

from django.db import models
from datetime import datetime

# Create your models here.
class StartUpInfo(models.Model):
    Name=models.CharField(max_length=100)
    TeamMemebersNumber=models.CharField(max_length=100)
    About=models.TextField()
    HeadQuarters=models.CharField(max_length=100)
    ProductVideo=models.CharField(max_length=100)
    WebsiteLink=models.CharField(max_length=100)
    Founders=models.CharField(max_length=100)
    FundingInfo=models.TextField()
    Team=models.CharField(max_length=50)
    DateTime=models.DateTimeField()
    
class Activites(models.Model):
    StartUpId=models.ForeignKey(StartUpInfo,on_delete=models.CASCADE)
    Info=models.TextField()
    TimeStamp=models.DateTimeField()

class TechCategories(models.Model):
    StartUpId=models.ForeignKey(StartUpInfo,on_delete=models.CASCADE)
    Info=models.CharField(max_length=100)
    TimeStamp=models.DateTimeField()



