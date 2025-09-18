from django.contrib import admin
from django.urls import path,include
from student.views import add_student,select_student,select2_student,select3_high,upsqldate,delete_data
urlpatterns = [
    path('add/',add_student),
    path('select/',select_student),
    path('vague_select/',select2_student),
    path('select3/',select3_high),
    path('update/',upsqldate),
    path('delete/',delete_data)
] 