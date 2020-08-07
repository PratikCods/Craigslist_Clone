from django.shortcuts import render,reverse

def home(request):
    return render(request,'my_app/base.html')
