from rest_framework import serializers
from companies.models import Company
from assets.serializers import AssetSerializer
from projects.serializers import ProjectSerializer
from teams.serializers import TeamSerializer
from accounts.serializers import UserSerializer


class CompanySerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    projects = ProjectSerializer(read_only=True, many=True)
    teams = TeamSerializer(read_only=True, many=True)
    assets = AssetSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'ceo', 'email', 'address', 'users', 'projects', 'teams', 'assets']
