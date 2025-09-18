from django.db import models
from django.utils import timezone
# Create your models here.



#表类
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    sex_choices = (
        (0,'女'),
        (1,'男'),
        (2,'保密')
    )

    name = models.CharField(max_length=32,unique=True,verbose_name='姓名')
    age = models.SmallIntegerField(verbose_name='年龄')
    sex = models.SmallIntegerField(verbose_name='性别',choices=sex_choices)
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    classmate = models.CharField(db_column='class',max_length=5,db_index=True, verbose_name='班级',default='')
    description = models.TextField(default='',verbose_name='个性签名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    chinese_socre=models.IntegerField(default=100)
    math_socre = models.IntegerField(default=100)

    class Meta:
        db_table = 'db_student'
    def __str__(self):
        return self.name +' '+str(self.age)
    