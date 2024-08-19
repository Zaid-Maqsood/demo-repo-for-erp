from django.contrib import admin
from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['company', 'team', 'project_name', 'client_name', 'start_time', 'end_time', 'project_status']

