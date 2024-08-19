from rest_framework import serializers
from accounts.models import User
from companies.models import Company
from teams.models import Team


class UserSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ['id', 'name', 'type', 'date_of_join', 'team', 'company']