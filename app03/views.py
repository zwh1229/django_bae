from django.shortcuts import render,HttpResponse
# Create your views here.



def index(request,mobile):
    
    print(type(mobile))
    return HttpResponse(f'{mobile}')