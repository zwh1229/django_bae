from django.shortcuts import render,HttpResponse
from .models import Student,StudentDetail,Course,Clas
# Create your views here.
def add_student(request):
    #一对多/一对一关联记录
    # stu = Student.objects.create(name="王五", age=24, sex=1, clas_id=2, stu_detail_id=3)
    # print(stu.name)
    # print(stu.clas.name)
    # print(stu.stu_detail.tel)
    #多对多的关联记录的增删改查
    #方式1
    # stu = Student.objects.create(name='rain',age=33,sex=1,clas_id=3,stu_detail_id=4)
    # c1 = Course.objects.get(title= '思修')
    # c2 = Course.objects.get(title= '逻辑学')
    #方式2
    # stu = Student.objects.get(name ='李四')
    # print('c1',c1)
    # print('c2',c2)
    # stu.courses.add(5,9)
    #方式3  客户端一般传列表
    # stu = Student.objects.get(name = '张三')
    # stu.courses.add(*[6,8])

    #删除
    # stu = Student.objects.get(name = '张三')
    # # stu.courses.remove(6)
    # #remove 也可以用列表这个
    # stu.courses.remove(*[6,8])

    #清除方法 clear   #清除关于这个rain的所有
    # stu = Student.objects.get(name = 'rain')
    # stu.courses.clear()

    #重置
    stu = Student.objects.get(name='李四')
    stu.courses.set([2,6,7,5,8])
    #查询
    course = stu.courses.all()
    print('course',course)
    course = stu.courses.all().values('title')
    print('course',course)

    return HttpResponse('添加关联记录成功')