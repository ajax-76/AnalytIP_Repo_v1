"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse
#from .forms import UploadFileForm
from django import forms
from app.FileRead import handle_uploaded_file



def home(request):
    
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })

def Hello(request):
    return render(request,'app/Hello.html')


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

class UploadFileForm(forms.Form):
    file = forms.FileField()


def Upload(request):
    try:
        if request.method == 'POST':
           file = UploadFileForm(request.POST,request.FILES)
           if file.is_valid():
              handle_uploaded_file(request.FILES['file'])
              return HttpResponse("Done")
    except Exception as e:
        return HttpResponse("Hrllo")
    return HttpResponse("Hrllo")
        
 


def FileUpload(request):
       return render(request,'app/FileUpload.html')


