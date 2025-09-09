from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse


def article_detail(request):


    return HttpResponse('2012/12文章')


def article_archive(request,year,month):
    print(year)
    print(month)
    return HttpResponse(f'{year},{month}文章')


def artiicle_archive_by_month(request,month,year):

    return  HttpResponse(f'{year}:{month}')