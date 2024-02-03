from django.shortcuts import render

# Create your views here.
def new_application(request):
    return render(request, 'account/new_application.html')
