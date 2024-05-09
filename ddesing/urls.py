"""
URL configuration for ddesing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front, name='front'),
    path('1/', task_1, name='task_1'),
    path('3/', task_3, name='task_3'),
    path('4/', task_4, name='task_4'),
    path('4/result/', task_4_1, name='task_4_1'),
    path('6/', task_6, name='task_6'),
    path('12/', task_12, name='task_12'),
    path('16/', task_16, name='task_16'),
    path('19/', task_19, name='task_19'),
    path('24_1/', task_24_1, name='task_24_1'),
    path('24_2/', task_24_2, name='task_24_2'),
    path('39/', task_39, name='task_39'),
    path('42/', task_42, name='task_42'),
    path('43/', task_43, name='task_43'),
    path('46/', task_46, name='task_46'),
    path('57/', task_57, name='task_57'),
    path('59/', task_59, name='task_59'),
    path('62_1/', task_62_1, name='task_62_1'),
    path('62_2/', task_62_2, name='task_62_2'),
    path('63/', task_63, name='task_63')
]
