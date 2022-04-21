from django.shortcuts import render,redirect,HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,"index.html")