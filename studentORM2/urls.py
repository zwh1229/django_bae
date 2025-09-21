from django.contrib import admin
from django.urls import path,include
from studentORM2.views import add_student,select_student,select_student2,index
urlpatterns = [
    # path('add/',add_student),
    # path('select/',select_student),
    # path('select2/',select_student2)
    path('',index)

] 