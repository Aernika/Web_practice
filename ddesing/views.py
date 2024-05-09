from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.core import mail


def front(request):
    return render(request, 'front.html', locals())


def task_1(request):
    return render(request, '1.html', locals())


def task_3(request):
    return render(request,'3.html',locals())


def task_4(request):
    return render(request,'4.html',locals())


def task_4_1(request):
    return render(request,'4_result.html',locals())


def task_6(request):
    return render(request,'6.html',locals())


def task_12(request):
    return render(request,'12.html',locals())


def task_16(request):
    return render(request,'16.html',locals())


def task_19(request):
    return render(request,'19.html',locals())


def task_24_1(request):
    return render(request,'24_1.html',locals())


def task_24_2(request):
    return render(request,'24_2.html',locals())


def task_39(request):
    return render(request,'39.html',locals())


def task_42(request):
    return render(request,'42.html',locals())


def task_43(request):
    return render(request,'43.html',locals())


def task_46(request):
    return render(request,'46.html',locals())


def task_57(request):
    return render(request,'57.html',locals())


def task_59(request):
    return render(request,'59.html',locals())


def task_62_1(request):
    return render(request,'62_1.html',locals())


def task_62_2(request):
    return render(request,'62_2.html',locals())


def task_63(request):
    return render(request,'63.html',locals())


