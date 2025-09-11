from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
# Create your views here.



'''
请求方式 /http /版本号

请求体
'''
def index(request):
    #获取请求方式
    # print(request.method)
    # #获取请求数据
    # print(request.body)
    # #数据是 urlencoded
    # print(request.POST)
    # #如果一个键多个值 可以用getlist

    # #获取get的
    # print(request.GET) #参数加载params

    # #获取请求路径
    # request.path  #永远是路径
    # request.get_full_path #全部的路径 带数据

    # #请求头
    # request.META  #再去获得哪个头 再加get
    # res = HttpResponse("ok")
    # res["user"]='haoge
    # return res
    

    #响应json数据
    # book = [{"title":'123','price':123}]
    # import json
    # #如果是多个键值对 用dumps
    # # return HttpResponse(json.dumps(book,ensure_ascii=False),content_type = 'application/json')
    # return JsonResponse(book)

    #如果返回的不是字典  
    book = [{"title":'123','price':123}, {"title":'123','price':123}]
    # return JsonResponse(book,safe=False)
    #获取地址
    remote_addr = request.META.get('REMOTE_ADDR')
    print(remote_addr)
    return render(request,'users/index.html',{'ip':remote_addr})



def login(request):
    return render(request,'users/login.html')


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def auth(request):

    #获取数据
    print('request.POST:',request.POST)
    user = request.POST.get('username')
    pwd = request.POST.get("password")
    if user =='haoge'and pwd=='123':
        return redirect('/user/')
    else:
        msg = '用户名或者密码错误'
        # return redirect('/user/login/')
        #静态页面不适合重定向

        return render(request,'users/login.html',{
        'msg':msg
        })