from django.contrib import admin
from django.urls import path,re_path,include
from day01.app01 import views
urlpatterns = [
    # 请求路径和视图函数的映射关系，一旦请求路径和某个path匹配 则执行这个path 的视图函数
    # path('admin/', admin.site.urls),
    path('timer/',views.get_timer),
    path('',views.index),
]
