from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from User import models
from User import sendEmail


# Create your views here.
def index(request):
    return render(request, 'User/index.html')


# 注册
def sign_up(request):
    if request.method == "GET":
        return render(request, 'User/sign_up.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('inputEmail')
        password1 = request.POST.get('inputPassword')
        verifyCode = request.POST.get('emailVerify')
        if 'signup' in request.POST:
            user1 = models.User.objects.filter(email=email)
            user2 = models.User.objects.filter(name=username)
            if user1:
                return render(request, 'User/sign_up.html', {'register_err': "邮箱已经用于注册"})
            elif user2:
                return render(request, 'User/sign_up.html', {'register_err': "用户名已存在"})
            elif verifyCode != request.session['verifyCode'] and request.session['verifyCode'] != None and request.session['username'] == username:
                return render(request, 'User/sign_up.html', {'register_err': "邮箱验证码不正确"})
            else:
                models.User.objects.create(email=email, password=password1, name=username)
                return render(request, 'User/sign_in.html')
        elif "emailVerify" in request.POST:
            verifycode = sendEmail.random_str();
            request.session['username'] = username;
            request.session['verifyCode'] = verifycode;
            sendEmail.send_register_email(email, verifycode, "register")
            return render(request, 'User/sign_up.html',{})


# 登陆
def sign_in(request):
    if request.method == "GET":
        return render(request, 'User/sign_in.html')
    else:
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        user = models.User.objects.filter(email=email, password=password).first()
        # user = models.User.objects.get(email=email, password=password)

        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.name
            request.session['email'] = user.email
            request.session.set_expiry(600)
            print(user.id)
            return HttpResponseRedirect('/User/index/')

        else:
            return render(request, 'User/sign_in.html',{'login_err': "用户名或密码错误"})


def sign_out(request):
    request.session.clear();
    return HttpResponseRedirect('/User/sign_in/');


def test(request):
    return render(request, 'User/sign_in.html')

