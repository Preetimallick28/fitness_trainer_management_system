from django.shortcuts import render

# Create your views here.
def registration_page(request):
    return render(request,'registration.html')


def login_(request):
    return render(request,'login.html')
