"""
URL configuration for django_base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from day01.app01 import views
from articles.views import article_detail,article_archive,artiicle_archive_by_month
urlpatterns = [
    # 请求路径和视图函数的映射关系，一旦请求路径和某个path匹配 则执行这个path 的视图函数
    # path('admin/', admin.site.urls),
    # path('timer/',views.get_timer),
    # path('',views.index),
    # path('articles/2012/12',article_detail),
    # re_path('articles/(\d{4})/(\d{2})/',article_archive)
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{1,2})/', artiicle_archive_by_month),
    path('home/',include('app03.urls'))
]
