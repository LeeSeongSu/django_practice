from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import *

class HabitAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Tester)
admin.site.register(Habit, HabitAdmin)
admin.site.register(Question)
