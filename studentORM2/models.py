from django.db import models

# Create your models here.

class Clas(models.Model):
    name = models.CharField(max_length=32,verbose_name='班级名称')
    class Meta:
        db_table = 'db_class'

class Course(models.Model):
    title = models.CharField(max_length=32,verbose_name='课程名称')
    class Meta:
        db_table = 'db_course'

    def __str__(self):
        return self.title

class Student(models.Model):
    sex_choices = (
        (0,'女'),
        (1,'男'),
        (2,'保密')
    )
    class Meta:
        db_table = "db_student2"


    name = models.CharField(max_length=32,unique=True,verbose_name='姓名')
    age = models.SmallIntegerField(verbose_name='年龄',default=18)
    sex = models.SmallIntegerField(choices=sex_choices)
    #创建一对多的关系  在数据库创建一个关联字段吧
    #级联   删除班级的信息 则引用外键额学生会一并被删除   
    #不添加外键约束  也就是不会强制关联
    clas = models.ForeignKey(to='Clas',on_delete=models.CASCADE,db_constraint=False)
    #多对多放在哪里都可以
    courses = models.ManyToManyField("Course",db_table='db_student2coures')
    #一对一关系 建立关联字段，在数据库中生成关联字段   一对多没区别 只是键名加了unique约束
    stu_detail = models.OneToOneField('StudentDetail',on_delete=models.CASCADE)

class StudentDetail(models.Model):
    tel = models.CharField(max_length=11)
    addr = models.CharField(max_length=22)
    class Meta:
        db_table = 'db_stu_detail'