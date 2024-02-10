from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import Application_Form
from .models import *

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def add_update_application(request, id=None):
    context = {}
    if id:
        application = get_object_or_404(Application, id=id)
        form  = Application_Form(instance=application)
        context['application'] = application
    else:
        form  = Application_Form(request.GET)
        if request.GET.get('course'):
            course = Course.objects.get(id=request.GET.get('course'))
            context['course'] = course
            form  = Application_Form(initial={'course': course})
    context['form'] = form
    
    if request.method == 'POST':
        if id:
            form  = Application_Form(request.POST, instance=application)
        else:
            form  = Application_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
        else:
            return HttpResponse(form.errors)
    
    return render(request, 'application/add_application.html', context)


def application_list(request):
    all_course = Course.objects.all()
    context = {'all_course': all_course}
    
    course_id = request.GET.get('course')
    search = request.GET.get('search')
    status = request.GET.get('status')
    batch = request.GET.get('batch')
    
    if course_id:
        select_course = Course.objects.get(id=course_id)
        course_batch = Batch.objects.filter(course=select_course)
        context['course_batch'] = course_batch
        context['select_course'] = select_course
    if search:
        context['search'] = search
    if status:
        context['status'] = status
    if batch:
        batch = get_object_or_404(Batch, id=batch)
        context['batch'] = batch
        
    
    if course_id and course_batch and status and search:
        application = Application.objects.filter(name__icontains=search, course=select_course, batch=batch, application_status=status)
    elif course_id and status and search:
        application = Application.objects.filter(name__icontains=search, course=select_course, application_status=status)
    elif course_id and search:
        application = Application.objects.filter(name__icontains=search, course=select_course)
    elif search:
        application = Application.objects.filter(name__icontains=search)
    elif status:
        application = Application.objects.filter(application_status=status)
    elif course_id and batch:
        application = Application.objects.filter(course=select_course, batch=batch)
    elif batch:
        application = Application.objects.filter(batch=batch)
    elif course_id:
        application = Application.objects.filter(course=select_course)
    else:
        application = Application.objects.all()
    
    context['application'] = application
    
    return render(request, 'application/application.html', context)





