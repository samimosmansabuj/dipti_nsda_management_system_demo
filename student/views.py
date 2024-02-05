from django.shortcuts import render, redirect, get_object_or_404
from .models import Student_Profile, Student_Attendance
from .forms import Student_Form, Student_Filter_Form
from account.models import Custom_User
from django.db.models import Q

# Create your views here.
def student_list(request):
    context = {}
    filter_form = Student_Filter_Form(request.GET)
    
    if filter_form.is_valid():
        if filter_form.cleaned_data['batch'] or filter_form.cleaned_data['course'] or filter_form.cleaned_data['search']:
            batch = filter_form.cleaned_data['batch']
            course = filter_form.cleaned_data['course']
            search = filter_form.cleaned_data['search']
            if batch and course and search:
                print('all filter')
                student = Student_Profile.objects.filter(Q(name__icontains=search) | Q(phone_number__icontains=search) | Q(last_education__icontains=search) & Q(batch=batch) & Q(course=course))
            elif batch and course:
                student = Student_Profile.objects.filter(batch=batch, course=course)
            elif batch:
                student = Student_Profile.objects.filter(batch=batch)
            elif course:
                student = Student_Profile.objects.filter(course=course)
            elif search:
                student = Student_Profile.objects.filter(Q(name__icontains=search) | Q(phone_number__icontains=search) | Q(last_education__icontains=search))
        else:
            student = Student_Profile.objects.all()
        
    context['student'] = student
    context['filter_form'] = filter_form
    
    return render(request, 'student/student_list.html', context)

def student_attendance(request):
    return render(request, 'student/student_attendance.html')

def add_student(request, id=None):
    context = {}
    if id:
        student = get_object_or_404(Student_Profile, id=id)
        context['student'] = student
        form = Student_Form(instance=student)
    else:
        form = Student_Form()
    context['form'] = form
    
    if request.method == 'POST':
        if id:
            form = Student_Form(request.POST, instance=student)
            if form.is_valid():
                student = form.save()
                return redirect('student_list')
        else:
            form = Student_Form(request.POST)
            if form.is_valid():
                student = form.save()
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                user = Custom_User.objects.create_user(username=username, password=username, email=email, user_type='Student')
                student.student_ID = user
                student.save()
                return redirect('student_list')
            
    
    return render(request, 'student/add_student.html', context)
