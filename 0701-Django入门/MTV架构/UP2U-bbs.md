# UP2U-bbs项目

# 创建项目

进入工程目录，使用控制台创建。使用命令：  
```django-admin startproject 项目名称```

>注意：项目名称不能使用 连接符（-）

code 项目名称

cd 项目名称

启动简易服务器

```python manage.py runserver```

# 创建应用

进入项目的根目录，使用以下命令创建应用：

```python manage.py startapp 应用名```

添加 视图（views） 

添加应用的 urls

添加工程的 urls

启动简易服务器

```python manage.py runserver```

# 数据库

## 创建模型 model

polls/models.py

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## 激活模型

在文件 **项目目录名/settings.py** 中 **INSTALLED_APPS** 子项添加点式路径后，它看起来像这样：

```py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

储存迁移

```cmd
python manage.py makemigrations polls
```

polls 可省略

执行迁移

```cmd
python manage.py migrate
```

## Django 管理界面

创建一个能登录管理页面的用户。请运行下面的命令：

```python manage.py createsuperuser```

依次输入用户名、邮箱（可选）、密码

创建完成后，重启开发服务器

### 向管理员界面添加投票界面

打开 **polls/admin.py** 文件，把它编辑成下面这样：

polls/admin.py

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

等待程序自动加载更改，如果加载失败，重启服务器：

```python manage.py runserver```

# 视图

添加以下：待投票问题详情、投票结果、投票，三个视图。这里直接使用**通用视图**。

polls.views.py

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 重新显示问题的投票表单
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "没有选择选项"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

修改 URLconf。这里在根 URLconf 中添加**命名空间**。

polls/urls.py

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

# 模板

由视图代码可知，我们需要三个模板。路径如下：

- polls/templates/polls/detail.html
- polls/templates/polls/results.html
- polls/templates/polls/index.html


**detail()**，它向模板传递了上下文变量 **question**。下面是 **polls/detail.html** 模板里正式的代码：

polls/templates/polls/detail.html

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>问题列表</title>
</head>

<body>
    <h1>{{ question.question_text }}</h1>
    <!-- <ul>
        {% for choice in question.choice_set.all %}
            <li>{{ choice.choice_text }}</li>
        {% endfor %}
    </ul> -->
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    <form action="{% url 'polls:vote' question.id %}" method="post">
        {% csrf_token %}
        {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">
            {{ choice.choice_text }}
        </label>
        <br>
        {% endfor %}
        <input type="submit" value="Vote">
    </form>
</body>

</html>
```

polls/templates/polls/results.html

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>问题列表</title>
</head>

<body>
    <h1>{{ question.question_text }}</h1>
    <ul>
        {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }} -- {{ choice.votes }}vote{{ choice.votes|pluralize }}</li>
        {% endfor %}
    </ul>

    <a href="{% url 'polls:detail' question.id %}"></a>
</body>

</html>
```

polls/templates/polls/index.html

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>问题列表</title>
</head>

<body>
    {% if latest_question_list %}
    <ul>
        {% for question in latest_question_list %}
        <!-- <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li> -->
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
        {% endfor %}
    </ul>
    {% else %}
    <p>没有 polls 可用</p>
    {% endif %}
</body>

</html>
```

# bbs 项目

这里直接复制 polls 的文件，并修改设置。

修改配置

修改文件：

- bbs/apps.py
- bbs/urls.py
- bbs/views.py
- UP2U_BBS/up2u_bbs/settings.py
- UP2U_BBS/up2u_bbs/urls.py

修改目录

- bbs/template/polls

## 添加新代码，完成 BBS

修改模型

- bbs/models.py

