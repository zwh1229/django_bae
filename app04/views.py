from django.shortcuts import render

# Create your views here.




def index(request):
    name =  'root'
    age =22
    is_marrired = False
    book_list = ['三国演义','水浒传']
    content = '13739715733'
    score  = 100
    return render(request,'app01/index.html',locals())  #测试的时候用比较合适locals把变量一一对应
