from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserForm


# Create your views here.
def custom_login(request):
    if request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        # 验证用户是否合法
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                # 登录
                login(request, user)
                return HttpResponseRedirect(reverse('todo:home'))
            else:
                return render(request, 'accounts/login.html', {'error_message': '用户未激活，请联系管理员处理'})
        # 返回页面
        else:
            return render(request, 'accounts/login.html', {'error_message': '用户名或密码错误'}) 


    return render(request, 'accounts/login.html')

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo:home'))


def custom_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        # 数据合法，保存到user
        user = form.save(commit=False)
        print(form.cleaned_data)
        user.set_password(form.cleaned_data['password'])
        user.save()

        # login自动识别请求及user表单中的信息
        login(request, user)
        return HttpResponseRedirect(reverse('todo:home',))

    context={'form': form}
    return render(request, 'accounts/register.html', context)
