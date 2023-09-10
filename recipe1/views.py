from django.shortcuts import render

# Create your views here.

def recipe1(request):
    return render(request,"recipepage1.html")