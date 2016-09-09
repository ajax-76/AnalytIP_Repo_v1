"""
Definition of models.
"""

from django.db import models

# Create your models here.
class StartUpInfo(models.Model):
    Name=models.CharField
    TeamMemebersNumber=models.CharField
    About=models.CharField
    HeadQuarters=models.CharField
    ProductVideo=models.CharField
    WebsiteLink=models.CharField


