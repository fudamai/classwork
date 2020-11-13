import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View, CreateView, UpdateView, DetailView
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Todo
from siteinfo.models import Footer, Col, Item, Banner
from .forms import TodoForm, TodoModifiForm

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            print(self.request.user)
            print()
            queryset = queryset.filter(author=self.request.user)
        else:
            queryset = queryset.filter(id=1)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        start_week = today - datetime.timedelta(today.weekday()) + datetime.timedelta(days=7)  # 当日日期减去周几加上七天，即为下一周第一天

        end_week = start_week + datetime.timedelta(days=7)

        todo_list = self.get_queryset()

        context['todo_today'] = todo_list.filter(duedate__day=today.day, duedate__month=today.month)
        context['todo_tomorrow'] = todo_list.filter(duedate__day=tomorrow.day, duedate__month=tomorrow.month)
        context['todo_next_week'] = todo_list.filter(duedate__range=[start_week, end_week])

        context['todo_doing'] = todo_list.filter(finish='doing', duedate__gte=today)
        context['todo_done'] = todo_list.filter(finish='done')
        context['todo_overdue'] = todo_list.filter(finish='doing', duedate__lt=today)
        
        context['siteinfo'] = {
            'footer' : Footer.objects.all().first(),
            'banner' : Banner.objects.all().first()
        }
        context['add_form'] = TodoForm()
        context['modifi_form'] = TodoModifiForm()
        context['current_user'] = {'user': self.request.user, 'is_login': self.request.user.is_authenticated}

        return context

@method_decorator(login_required, name='post')
class TodoUpdateView(View):

    def post(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        key = request.POST['key']
        if key == 'update1':
            todo.duedate =  datetime.date.today() + datetime.timedelta(days=1)
        elif key == 'update2':
            todo.duedate =  datetime.date.today() + datetime.timedelta(days=7)

        todo.save()
        return redirect('todo:home')


@method_decorator(login_required, name='post')
class TodoModifiView(View):

    def post(self, request, id, *args, **kwargs):
        todo = get_object_or_404(Todo, id=id)
        title = request.POST['title']
        content = request.POST['content']
        print(title)
        if title and content:
            todo.title = title
            todo.content = content
            todo.save()
        return redirect('todo:home')


@method_decorator(login_required, name='post')
class TodoAddView(CreateView):
    model = Todo
    template_name = 'todo/index.html'
    fields = ('title', 'content', 'important', 'duedate')

    def post(self, request, *args, **kwargs):
        form = TodoForm(self.request.POST)
        print(form)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = self.request.user
            todo.save()
        return redirect('todo:home')      


@method_decorator(login_required, name='post')
class TodoDeleteView(View):

    def post(self, request, id, **kwargs):
        todo = get_object_or_404(Todo, id=id)
        todo.delete()

        return redirect('todo:home')


@method_decorator(login_required, name='post')
class TodoCheckView(View):
    
    def post(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        finish = request.POST['finish']
        print(finish)
        if finish:
            todo.finish = finish
            todo.save()  # 更改对象时需保存
        return redirect('todo:home')


class TodoQueryView(ListView):
    model = Todo
    template_name = 'todo/query_page.html'
    context_object_name = 'todo_query_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        # print(queryset)
        query = self.request.GET.get('q')
        # print(query)
        # 用户未登录，返回查询结果为空
        if self.request.user.is_authenticated:
            if query:
                return queryset.filter(
                    Q(title__icontains=query) |
                    Q(content__icontains=query)
                ).distinct()
        else:
            queryset = ''
        return queryset

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['siteinfo'] = {
            'footer' : Footer.objects.all().first(),
            'banner' : Banner.objects.all().first()
        }

        return context