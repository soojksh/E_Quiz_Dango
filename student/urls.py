from django.urls import path
from .import views

urlpatterns = [
    path('studentclick/', views.studentclick, name="studentclick"),
]
