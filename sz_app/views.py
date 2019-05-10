from django.shortcuts import render, redirect, HttpResponse
import re
from sz_app import models
import json
from .tasks import send_mail
import random
from sz_app import tasks
# Create your views here.


def random_num():
    list_random = []
    for i in range(6):
        num = str(random.randint(0, 9))
        list_random.append(num)
    nums = ''.join(list_random)
    return nums


def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return HttpResponse("请先<a href='/index'>登录</a>！！")

    return inner


def index(req):
    if req.method == 'POST':
        post_name = req.POST.get('post_name')
        response = {"status": False, "username": None, 'msg': None, 'code': None}
        if post_name == "sign_in":
            try:
                username = req.POST.get('username')
                password = req.POST.get('password')
                if models.UserInfo.objects.filter(email=username).count():
                    check = models.UserInfo.objects.filter(email=username, password=password).count()
                    print(username, password)
                    if check:
                        print("验证成功")
                        req.session['is_login'] = True
                        req.session['username'] = username
                        name = models.UserInfo.objects.filter(email=username).values('name')[0]['name']
                        req.session['name'] = name
                        response['status'] = True
                        response['username'] = name
                        response['msg'] = "ok"
                        return HttpResponse(json.dumps(response, ensure_ascii=False))
                    else:
                        response['msg'] = '账号或密码错误。'
                        return HttpResponse(json.dumps(response, ensure_ascii=False))
                else:
                    response['msg'] = '账号不存在，请先注册。'
                    return HttpResponse(json.dumps(response, ensure_ascii=False))
            except:
                return HttpResponse("请刷新页面。")
        elif post_name == "sign_up":
            username = req.POST.get('username', None)
            password = req.POST.get('password', None)
            name = req.POST.get('name', None)
            if models.UserInfo.objects.filter(email=username).count():
                response['msg'] = "邮箱已注册，请更换其他邮箱。"
                return HttpResponse(json.dumps(response, ensure_ascii=False))
            else:

                models.UserInfo.objects.create(
                    email=username,
                    password=password,
                    name=name
                )
                print("信息保存成功")
                response['username'] = name
                response['msg'] = "恭喜您：" + name + "，注册成功"
                response['status'] = True
                return HttpResponse(json.dumps(response, ensure_ascii=False))
        elif post_name == "set_username":
            set_username = req.POST.get('username', None)
            if models.UserInfo.objects.filter(email=set_username).count():
                response['msg'] = "邮箱已注册，请更换其他邮箱。"
                return HttpResponse(json.dumps(response, ensure_ascii=False))
        else:
            nums = random_num()
            email = req.POST.get('username')
            email_list = [email, ]
            send_mail.delay(email_list, nums)
            response['code'] = nums
            print(nums)
            return HttpResponse(json.dumps(response, ensure_ascii=False))

    return render(req, 'index.html')


def dsri(req):
    return render(req, "dsri.html")


def start(req):
    if req.method == "POST":
        url = req.POST.get("url")
        try:
            new_url = re.search("/[a-z]+/", url).group()
            return redirect(new_url)
        except:
            return redirect("/index/")
    return render(req, "start.html")


def city(req, menu1):
    try:
        if menu1:
            return render(req, menu1 + '.html')
        else:
            return render(req, "city.html")
    except:
        return render(req, "city.html")


def news(req, menu2):
    try:
        if menu2:
            return render(req, menu2 + '.html')
        else:
            return render(req, "news.html")
    except:
        return render(req, "news.html")


def case(req, menu):
    try:
        if menu:
            return render(req, menu + '.html')
        else:
            return render(req, "case.html")
    except:
        return render(req, "case.html")


@auth
def download(req):
    return render(req, "download.html")


def logout(req):
    req.session.clear()
    return redirect("/index")
