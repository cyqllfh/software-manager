from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Software(models.Model):
    name = models.CharField(max_length=50)
    ins_cmd = models.CharField(max_length=200)
    uins_cmd = models.CharField(max_length=200)
    start_cmd = models.CharField(max_length=100)
    stop_cmd = models.CharField(max_length=100)
    status_cmd = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)

class Machine(models.Model):
    ip = models.GenericIPAddressField()
    alias = models.CharField(max_length=1000)
    remark = models.CharField(max_length=100)
   
class ConfigModel(models.Model):
    software = models.ForeignKey(Software)
    tar_path = models.CharField(max_length=200)
    def_parm = models.TextField()
    
