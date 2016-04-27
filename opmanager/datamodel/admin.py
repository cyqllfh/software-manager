from django.contrib import admin
from datamodel.models import Software,Machine,ConfigModel,Script

# Register your models here.
class SoftwareAdmin(admin.ModelAdmin):
  list_display = (
                   'name', 'ins_cmd', 'uins_cmd', 'start_cmd', 'stop_cmd',
                   'status_cmd', 'remark'
                 )
class MachineAdmin(admin.ModelAdmin):
    list_display = ('ip', 'alias', 'remark')

class ConfigModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'tar_pkg')

class ScriptAdmin(admin.ModelAdmin):
    list_display = ('id','script_file', 'remark')
    filter_horizontal = ('machines',)

admin.site.register(Software, SoftwareAdmin)
admin.site.register(Machine, MachineAdmin)
#admin.site.register(ConfigModel, ConfigModelAdmin)
admin.site.register(ConfigModel)
admin.site.register(Script, ScriptAdmin)
