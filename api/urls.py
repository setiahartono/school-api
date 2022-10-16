from django.urls import path
from api import views


urlpatterns = [
    path('schools/', views.SchoolListCreateApi.as_view()),
    path('schools/<int:pk>/', views.SchoolUpdateApi.as_view()),
]