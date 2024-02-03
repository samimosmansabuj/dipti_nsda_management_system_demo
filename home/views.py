from django.shortcuts import render, redirect, get_object_or_404
from .forms import Application_Form
from .models import *

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def add_application(request, id=None):
    context = {}
    if id:
        application = get_object_or_404(Application, id=id)
        form  = Application_Form(instance=application)
        context['application'] = application
    else:
        form  = Application_Form()
    context['form'] = form
    
    if request.method == 'POST':
        if id:
            form  = Application_Form(request.POST, instance=application)
        else:
            form  = Application_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    
    return render(request, 'application/add_application.html', context)


def application_list(request):
    all_course = Course_Name.objects.all()
    all_batch = Batch.objects.all()
    context = {'all_batch': all_batch, 'all_course': all_course}
    
    course_id = request.GET.get('course')
    batch_id = request.GET.get('batch')
    status = request.GET.get('status')
    
    if course_id and batch_id and status:
        course_id = get_object_or_404(Course_Name, id=course_id)
        batch_id = get_object_or_404(Batch, id=batch_id)
        application = Application.objects.filter(course=course_id, batch=batch_id, application_status=status)
    elif status:
        application = Application.objects.filter(application_status=status)
    elif course_id and batch_id:
        course_id = get_object_or_404(Course_Name, id=course_id)
        batch_id = get_object_or_404(Batch, id=batch_id)
        application = Application.objects.filter(course=course_id, batch=batch_id)
    elif batch_id:
        batch_id = get_object_or_404(Batch, id=batch_id)
        application = Application.objects.filter(batch=batch_id)
    elif course_id:
        course_id = get_object_or_404(Course_Name, id=course_id)
        application = Application.objects.filter(course=course_id)
    else:
        application = Application.objects.all()
    
    context['application'] = application
    context['course_id'] = course_id
    context['batch_id'] = batch_id
    context['status'] = status
    
    return render(request, 'application/application.html', context)





