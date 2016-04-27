from django.contrib import admin
from datamodel.models import Software,Machine,ConfigModel

# Register your models here.
class SoftwareAdmin(admin.ModelAdmin):
  list_display = (
                   'name', 'ins_cmd', 'uins_cmd', 'start_cmd', 'stop_cmd',
                   'status_cmd', 'remark'
                 )
class MachineAdmin(admin.ModelAdmin):
    list_display = ('ip', 'alias','remark')

class ConfigModelAdmin(admin.ModelAdmin):
    list_display = ('id','tar_pkg',)

admin.site.register(Software, SoftwareAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(ConfigModel, ConfigModelAdmin)
