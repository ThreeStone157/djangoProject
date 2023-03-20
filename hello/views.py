from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def hello_world(request, month):
    print("现在是{}月".format(month))
    return HttpResponse("hello World!")


def hello_china(request):
    return HttpResponse("hello china~!~")


def test_html(request):
    print("请求方法：{}，请求头：{}，请求体：{}".format(request.method, request.headers, request.body))
    print("请求ip地址：{}".format(request.headers.get('User-Agent')))
    return render(request, "index.html")


# 重定向
def test_redirect(request):
    raise
    return redirect('not_404')


def not_404(request):
    return render(request, '404.html')

