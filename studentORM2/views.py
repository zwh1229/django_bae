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


def select_student(request):
    '''
    基于对象的关联查询 （子查询）
    '''
    #正向查询
    #一堆多关联
    #查询张三所在班级的名称
    stu = Student.objects.get(name = '张三')
    # print(stu.clas.name)
    #反向查询  班级里有哪些学生
    clas = Clas.objects.get(name = '计算机科学与技术2班')
    #反向查询1  #使用关联模型表名的小写
    # stu = clas.student_set.all()
    # print('stu',stu)
    #反向查询2  #在模型定义 related_name = 自定义表明   stu_list
    # print(clas.stu_list.all())

    #一对一查询
    #查询手机号110d的学生姓名和年龄
    #方式1  表名小写
    stu_detail = StudentDetail.objects.get(tel='110')
    # print(stu_detail.student.name)
    # print(stu_detail.student.age)
    #方式2  设置related_name
    # print(stu_detail.stu_desc.name)
    # print(stu_detail.stu_desc.age)

    #多对多
    # stu = Student.objects.get(name = '李四')
    # print(stu.courses.all())

    #反1  写表小明
    course = Course.objects.get(title = '近代史')
    # print(course.student_set.all())
    #反2 related_name
    print(course.stu_course.all())
    #还可以使用values 取想要的
    print(course.stu_course.all().values('age','name'))
    return HttpResponse('关联查询成功')


def select_student2(request):
    from  django.db.models import Avg,Count,Min,Max

    '''基于双下划线跨表查询 join '''
    '''
    正向直接用字段名
    反向用relate_name 或者_set
    '''
    # #查询张三年龄  
    # #点对点1快
    # #获取完整对象2合适
    # result1 = Student.objects.filter(name = '张三').values('age')
    # result2 = Student.objects.get(name = '张三')
    # # print('result1',result1)
    # # print('result2',result2.age)

    # # 查询大于22岁的学生姓名以及班级名称
    # # SELECT db_student2.name,db_class.name FROM db_student2 INNER JOIN db_class on db_student2.clas_id = db_class.id WHERE db_student2.age >22
    # #正
    # resutl = Student.objects.filter(age__gt=22).values('name','clas__name')
    # #反
    # result2 = Clas.objects.filter(stu_list__age__gt=22).values('stu_list__name','name')
    # # print('result1',result1)
    # # print('result2',result2)

    # #查询计算机科学与技术二班有哪些学生
    # result3 = Clas.objects.filter(name = '计算机科学与技术2班').values('stu_list__name')
    # retult4 = Student.objects.filter(clas_id = 2).values('name')
    # # print('result3',result3)
    # # print('retult4',retult4)

    # #李四所报的选修课名称
    # result5 = Student.objects.filter(name = '李四').values('courses__title')
    # result6 = Course.objects.filter(stu_course__name = '李四').values('title')
    # # print('result5',result5)
    # # print('result6',result6)
    # #查询了选修近代史这门课程学生的姓名和年龄
    # result7 = Student.objects.filter(courses__title = '近代史').values('name','age')
    # result8 = Course.objects.filter(title= '近代史').values('stu_course__name',"stu_course__age")
    # # print('result7',result7)
    # # print('result8',result8)
    # #查询一下李四的手机号
    # result9 = Student.objects.filter(name = '李四').values('stu_detail__tel')
    # result10 = StudentDetail.objects.filter(stu_desc__name = '李四').values('tel')
    # # print('result9',result9)
    # # print('result10',result10)

    # #查询手机号是110的学生的姓名和所在班级
    # result11 = StudentDetail.objects.filter(tel = 110).values('stu_desc__name','stu_desc__clas__name')
    # print('result11',result11)

    # result12 = Student.objects.filter(stu_detail__tel = 110).values('name','clas__name')
    # print('result12',result12)
    #查询每一个班级的名称以及学生名称   
    # ret = Clas.objects.values('name').annotate(made = Count('stu_list__name'))
    # # print('ret',ret)
    # ret1 = Student.objects.values('clas__name').annotate(c = Count('name'))
    # print('ret1',ret1)

    #查询每个学生的姓名，年龄以及选修课程个数
    print(Student.objects.values('name','age').annotate(c  = Count("courses__title")))
    #查询每个学生姓名以及选修课程个数并按着选秀课程个数排序
    print(Student.objects.all().annotate(c = Count('courses__title')).order_by("c").values('name','c'))
    return HttpResponse('join查询')


def index(request):


    return render(request,'student/index.html')