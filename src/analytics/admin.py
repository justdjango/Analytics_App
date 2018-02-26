from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import View

@admin.register(View)
class ViewAdmin(ImportExportModelAdmin):
	pass