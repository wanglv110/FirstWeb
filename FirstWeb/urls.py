"""FirstWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 注册一个新的url，第一个参数是url的名字(网页访问输入)，第二个参数是执行的函数
    # 不写默认是调用index接口
    path(r'', views.index, name='index'),

    path(r'scan', views.scan),

    path(r'scanCommit', views.scanCommit)
]
