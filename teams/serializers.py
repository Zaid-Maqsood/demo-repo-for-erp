from rest_framework import serializers
from teams.models import Team
from companies.models import Company


class TeamSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Team
        fields = ['id', 'team_name', 'company']

