from rest_framework import serializers

from api.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'capacity', 'address', 'phone_number')
