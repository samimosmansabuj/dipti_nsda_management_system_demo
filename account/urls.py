from django.urls import path
from .views import *

urlpatterns = [
    path('new-application/', new_application, name='new_application')
]
