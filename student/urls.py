from django.urls import path
from .views import *

urlpatterns = [
    path('add-student/', add_student, name='add_student'),
    path('update-student/<int:id>/', add_student, name='add_student'),
    path('student/', student_list, name='student_list'),
    path('student-attendance/', student_attendance, name='student_attendance'),
]
