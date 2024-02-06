from django.shortcuts import render, redirect, get_object_or_404
from .forms import Teacher_Form
from .models import Teacher, Custom_User

# Create your views here.
def new_application(request):
    return render(request, 'account/new_application.html')

def add_teacher(request, id=None):
    context = {}
    if id is not None:
        teacher = get_object_or_404(Teacher, id=id)
        form = Teacher_Form(instance=teacher)
        context['teacher'] = teacher
    else:
        form = Teacher_Form()
    context['form'] = form

    if request.method == 'POST':
        if id is not None:
            form = Teacher_Form(request.POST, instance=teacher)
            if form.is_valid():
                teacher = form.save()
            return redirect('teacher_list')
        else:
            form = Teacher_Form(request.POST)
            if form.is_valid():
                teacher = form.save()
                user = Custom_User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['username'], user_type='Teacher')
                teacher.teacher_user = user
                teacher.save()
                return redirect('teacher_list')

    return render(request, 'teacher/add_teacher.html', context)


def teacher_list(request):
    context = {}
    teacher_list = Teacher.objects.all()
    context['teacher_list'] = teacher_list


    return render(request, 'teacher/teacher_list.html', context)
