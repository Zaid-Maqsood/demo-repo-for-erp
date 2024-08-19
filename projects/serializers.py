from rest_framework import serializers

from companies.models import Company
from projects.models import Project
from teams.models import Team


class ProjectSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'company', 'project_name', 'client_name', 'start_time', 'end_time',
                  'project_status', 'team']
