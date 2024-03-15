from django.shortcuts import render

# Create your views here.
def studentclick(request):
    return render(request, 'student/studentclick.html')
