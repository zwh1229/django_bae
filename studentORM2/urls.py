from django.contrib import admin
from django.urls import path,include
from studentORM2.views import add_student
urlpatterns = [
    path('add/',add_student),

] 