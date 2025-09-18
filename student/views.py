from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import Student
def add_student(request):


    #方式1 实例化+save   模型类对象映射记录
    # stu  = Student(name='小黑',age=333,sex=1)
    # stu.save()
    # print(stu.id)
    # print(stu.name)
    # print(stu.age)


    #方式2  使用模型类.objects  返回值也是类对象
    stu = Student.objects.create(name ='saobi',age=25,sex=0,birthday='2020-2-9')
    print(stu.id)
    print(stu.name)
    print(stu.age)
    return HttpResponse('添加成功')

def select_student(request):
    # all函数：返回的一个Queryset 类似于一个list 的数据类型，里面的元素都是统一的
    #查所有
    # student_list = Student.objects.all()
    # print('student_list',student_list)

    # # first last返回第一个 最后一个
    # #还可以使用下标记
    # stu = Student.objects.first()
    # print(stu.name)
    # print(stu.age)

    # stu = Student.objects.last()
    # print(stu.name)
    # print(stu.age)
    # #filter方法 where语句
    # #即使是一个返回的也是Queryset对象
    # student_list = Student.objects.filter(sex=1,age=333)
    # print('studen_list',student_list)

    # #exclude排除符合条件的记录
    # #查寻除了老黑之外的所有学生

    # student_list= Student.objects.exclude(name='小黑')
    #get 方法  和filter 返回结果上不一样 查询结果必须是有且只有一条符合的  #查出多个报错 0个也报错
    
    # student_list = Student.objects.get(sex=0) 
    
    #oder_by 是queryset的内置方法   
    # student_list = Student.objects.all().order_by('-age')

    # #count 计数返回 int类型

    # count = Student.objects.all().count()
    # count1 = Student.objects.filter(sex=3).count()
    # print('count',count)
    # print('count1',count1)
    # #exist 判断是否存在记录
    # print(Student.objects.exists())
    #values values_list

    # student_list = Student.objects.all().values('name','age') #返回的是字典组成的
    # student_list_values_list = Student.objects.all().values_list('name','age')
    # print('student_list',student_list)
    # print('student_list_values_list',student_list_values_list)

    #distinct 去重 一般和valuse valuest_list 针对于某个字段使用  如果是全表唯一 靠数据库约束（unique=True）
    print(Student.objects.values('age').distinct().order_by('age'))
    return HttpResponse('') 

def select2_student(request):
    #模糊查询
    # #开头
    # stu_list = Student.objects.filter(name__startswith='张')
    # #结尾
    # stu_list1 = Student.objects.filter(name__endswith='豪')
    # #包含
    # stu_list2 = Student.objects.filter(name__contains='小')
    # print('stu_list',stu_list)
    # print('stu_list1',stu_list1)
    # print('stu_list2',stu_list2)

    #查询为空
    # stu_list = Student.objects.filter(birthday__isnull=True)
    # print('stu_list',stu_list)
    #查询大于 小于啥的
    # stu_list = Student.objects.filter(age__gt=30)
    

    #查询范围
    stu_list = Student.objects.filter(age__range=(20,25))
    print('stu_list',stu_list)
    return HttpResponse('模糊查询成功')


def select3_high(request):
    from django.db.models import F,Q,Sum,Count,Avg,Max,Min
    # #查询语文成绩大于数学成绩的学生
    # #比较两个字段  F函数
    # stu_list = Student.objects.filter(chinese_socre__gt = F('math_socre'))
    # # print(stu_list)
    # #Q函数 编写更复杂的逻辑 与或非
    # # stu_list = Student.objects.filter(sex=1,age=333)
    # # stu_list = Student.objects.filter(sex=1).filter(age = 333)
    # stu_list = Student.objects.filter(Q(age__gt=30)|Q(sex=0))

    # stu_list = Student.objects.filter(Q(age__gt=30)|~Q(sex=2)&~Q(sex=1))
    # # print(stu_list)
    # #聚合函数
    # ret = Student.objects.aggregate(avg = Avg('chinese_socre'))
    # print('ret',ret)

    #分组 annotate  group by   valuses对应的是group by字段
    # ret = Student.objects.values('sex').annotate(avg  = Avg('chinese_socre'))
    # print('ret',ret)
    

    #原生sql raw
    ret = Student.objects.raw('SELECT id,name FROM db_student')
    #只能用for 循环遍历读取
    print('ret',ret)
    for stu in ret:
        print(stu,type(stu),stu.name,stu.age)
    

    return HttpResponse('高阶查询成功')
def upsqldate(request):
    # #方式1 基于模型对象save
    # stu = Student.objects.get(name='赵华')
    # print(stu.name)
    # print(stu.age)
    # stu.chinese_socre=22
    # stu.save()  #只有save之后才会 执行这个方法效率很低 是把所有字段加进去再修改
    #方式2 queryset对象的update
    # Student.objects.filter(age__gt=30).update(chinese_socre=20,math_socre=30)

    #将年龄小于20的语文成绩降低20
    from django.db.models import F
    Student.objects.filter(age__lt=20).update(chinese_socre = F('chinese_socre')-20)
    return HttpResponse('更新成功')


def delete_data(request):
    #1 基于模型类操作
    #如果是按着主键删除可以参数按 pk=13
    # stu = Student.objects.get(id=13)
    # stu.delete()
    #基于queryset删除

 
    stu = Student.objects.filter(chinese_socre__lt=70).delete()
    print('stu',stu)
    return HttpResponse('删除成功')