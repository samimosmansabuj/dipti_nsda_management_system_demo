from django.urls import path
from .views import *

urlpatterns = [
    path('new-application/', new_application, name='new_application'),

    path('add-teacher/', add_teacher, name='add_teacher'),
    path('update-teacher/<int:id>/', add_teacher, name='update_teacher'),
    path('teacher/', teacher_list, name='teacher_list'),
]
