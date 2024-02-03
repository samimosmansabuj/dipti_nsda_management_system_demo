from django.shortcuts import render, redirect, get_object_or_404
from .models import Student_Profile, Student_Attendance
from .forms import Student_Form
from account.models import Custom_User

# Create your views here.
def student_list(request):
    return render(request, 'student/student_list.html')

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
