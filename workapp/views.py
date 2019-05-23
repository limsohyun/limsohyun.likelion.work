from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def preview1(request):
    return render(request,'preview1.html')

def preview2(request):
    return render(request,'preview2.html')
