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
    remark = models.CharField(max_length=100, blank=True)
    
    def __unicode__(self):
        return self.name

class Machine(models.Model):
    ip = models.GenericIPAddressField()
    alias = models.CharField(max_length=1000)
    remark = models.CharField(max_length=100, blank=True)
    
    def __unicode__(self):
        return self.ip
   
class ConfigModel(models.Model):
    software = models.ForeignKey(Software)
    tar_pkg = models.FileField(upload_to="files")
    def_parm = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.tar_pkg.name

class Script(models.Model):
    script_file = models.FileField(upload_to="scripts")
    machines = models.ManyToManyField(Machine, blank=True)
    remark = models.TextField(blank=True)    

    def __unicode__(self):
        return self.script_file.name
