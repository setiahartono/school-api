from rest_framework import serializers

from api.models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'id',
            'name',
            'capacity',
            'address',
            'phone_number'
        )
        read_only_fields = ['id']
    
    def validate_capacity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Capacity must be greater than zero")
        return value


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'school',
            'identification',
        )
        read_only_fields = ['id', 'identification']
    
    def validate(self, data):
        school = data['school']

        enrolled_student_count = Student.objects.filter(school=school).count()
        if enrolled_student_count + 1 > school.capacity:
            raise serializers.ValidationError("Can't register student - School reached full capacity")
        return data
