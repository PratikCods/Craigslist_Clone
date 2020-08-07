from django.shortcuts import render,reverse

def home(request):
    return render(request,'my_app/base.html')

def new_search(request):
    search = request.POST.get('search')
    return render(request,'my_app/new_search.html',{'search':search})
