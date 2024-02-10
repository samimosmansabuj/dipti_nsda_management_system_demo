from django.shortcuts import render, redirect, get_object_or_404
from .forms import Teacher_Form
from .models import Custom_User
from home.models import Teacher

# Create your views here.
def new_application(request):
    return render(request, 'account/new_application.html')

def add_teacher(request, id=None):
    context = {}
    return render(request, 'teacher/add_teacher.html', context)


def teacher_list(request):
    context = {}
    teacher_list = Teacher.objects.all()
    context['teacher_list'] = teacher_list
    return render(request, 'teacher/teacher_list.html', context)
