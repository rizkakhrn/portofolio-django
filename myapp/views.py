from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'myapp/profile.html')

def education(request):
    return render(request, 'myapp/education.html')

def social(request):
    return render(request, 'myapp/social.html')

def experience(request):
    return render(request, 'myapp/experience.html')