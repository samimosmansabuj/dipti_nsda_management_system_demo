from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add-application/', add_update_application, name='add_application'),
    path('update-application/<int:id>/', add_update_application, name='update_application'),
    path('application/', application_list, name='application_list'),
    
    
]
