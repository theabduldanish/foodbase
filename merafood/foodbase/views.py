from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,'foodbase/homepage.html')


def outlets(req):
    return render(req,'foodbase/outlets.html')    