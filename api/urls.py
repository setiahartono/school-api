from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers

from api import views


router = routers.SimpleRouter()
router.register(r'schools', views.SchoolViewsets)
router.register(r'students', views.StudentViewsets)

student_school_router = routers.NestedSimpleRouter(
    router,
    r'schools',
    lookup='schools'
)
student_school_router.register(
    r'students',
    views.StudentSchoolViewsets,
    basename='student-school'
)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(student_school_router.urls)),
]