from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
def get_timer(request):
    '''
    request :形参 所有请求参数
    return HttpResponse对象
    '''
    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %X")

    return render(request,"app01/timer.html",{'now':nowStr})

def index(request):

    #返回一个简单的字符串
    # return HttpResponse('我是你爹')
    return render(request,'app01/index.html')
# Create your views here.



