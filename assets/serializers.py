from rest_framework import serializers
from assets.models import Asset
from companies.models import Company


class AssetSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Asset
        fields = ['id', 'name', 'company']

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['company'] = str(instance.company)  # Replace with your desired output format
    #     return representation
