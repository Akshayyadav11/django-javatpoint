from django.template import loader
import datetime
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.forms.form import EmpForm

def hello(request):
    return HttpResponse('<h2>Hello World</h2>')

def index(request):  
    # now = datetime.datetime.now()  
    # html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    # return HttpResponse(html)
    # name = {  
    #     'student':'rahul'  
    # }  
    stdform = EmpForm()
    template = loader.get_template('index.html') # getting our template  
    return HttpResponse(template.render({'details':stdform}))

    # return render(request, 'index.html')