from rest_framework import viewsets

from api.models import School, Student
from api.serializers import SchoolSerializer, StudentSerializer


class SchoolViewsets(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentViewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentSchoolViewsets(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        qs = Student.objects.filter(school_id=self.kwargs['schools_pk'])
        return qs

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            kwargs['data']['school'] = self.kwargs['schools_pk']
        return super().get_serializer(*args, **kwargs)