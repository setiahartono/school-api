from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import School, Student
from api.serializers import SchoolSerializer


class SchoolListCreateApi(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
