import os

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Reply, Topic
from .forms import ReplyForm, TopicForm

# 使用基于类的通用视图实现
# method_decorator 装饰器，转换函数装饰器为防范装饰器
@method_decorator(login_required, name='post')
class IndexView(generic.ListView):
    model = Topic
    template_name = 'bbs/index.html'
    # # 定义上下文的键名
    context_object_name = 'topic_list'


    # 可以很方便地使用 get_queryset 来给查询集添加逻辑
    def get_queryset(self):
        """Return Topics."""
        queryset = super().get_queryset()
        print(queryset)
        query = self.request.GET.get('q')
        print(query)
        if query:
            return queryset.filter(
                Q(topic_text__icontains=query) |
                Q(author__username__icontains=query)
            ).distinct()
            
        return queryset.order_by('-pub_date')

    # 返回用于显示对象的上下文数据。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['current_user'] = {'user': self.request.user, 'is_login': self.request.user.is_authenticated}
        context['form'] = TopicForm()
        return context

    # 定义函数，操作帖子（topic）添加
    def post(self, *args, **kwargs):
        try:
            # 判断PK存在的情况下，只更新帖子
            pk= self.request.POST.get('pk')
            if pk:
                topic = get_object_or_404(Topic, pk=pk)
                # print('get topic by pk :', pk, topic)
                topic.topic_text = self.request.POST['topic_text']
                topic.save()

                return HttpResponseRedirect(reverse('bbs:detail', args=(topic.id,)))

            form = TopicForm(self.request.POST, self.request.FILES or None)
            # print(form)
            # 判断是否有值
            if form.is_valid():
                if self.request.FILES:
                    root, ext = os.path.splitext(str(self.request.FILES['picture']))
                    # print(self.request.FILES['picture'])
                    # print(ext)
                    if ext == '.jpg' or ext == '.png':
                        topic = form.save(commit=False)
                        topic.author = self.request.user
                        topic.save()
                    else:
                        context = {}
                        context['topic_list'] = self.get_queryset()
                        context['current_user'] = {'user': self.request.user, 'is_login': self.request.user.is_authenticated}
                        context['form'] = TopicForm()
                        context['error_message'] = '上传图片格式错误！'
                        return render(self.request, 'bbs/index.html', context)
                else:
                    topic = form.save(commit=False)
                    # print('Topic:', topic, type(topic))
                    topic.author = self.request.user
                    topic.save()
        except(KeyError):
            return render(self.request, 'bbs/index.html', {'topic_list': Topic.objects.all(), 'error_message': "传值出错！"})
        else:
            return HttpResponseRedirect(reverse('bbs:index',))


class DetailView(generic.DetailView):
    # DetailView 期望从 URL 中捕获名为 "pk" 的主键值，通过键值获得指定的 topic 并传给模板（template）。
    model = Topic
    template_name = 'bbs/detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 往上下文中添加一个topic_list
        context['topic_list'] = Topic.objects.all()
        context['current_user'] = {'user': self.request.user, 'is_login': self.request.user.is_authenticated}
        context['form'] = ReplyForm()
        return context

    def post(self,request, pk, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=pk)
        try:
            form = ReplyForm(self.request.POST, self.request.FILES or None)
            # print(form)
            if form.is_valid():
                if self.request.FILES:
                    root, ext = os.path.splitext(str(self.request.FILES['picture']))
                    # print(self.request.FILES['picture'])
                    # print(ext)
                    # 判断接受到的图片格式
                    if ext == '.jpg' or ext == '.png':
                        reply = form.save(commit=False)
                        # print('Reply:', reply, type(reply))
                        reply.topic = topic
                        reply.author = self.request.user
                        reply.save()
                    else:
                        return render(self.request, 'bbs/detail.html', {'topic': topic, 'error_message': "上传图片格式错误！",
                        'topic_list': Topic.objects.all(), 'current_user' : {'user': self.request.user, 'is_login': self.request.user.is_authenticated}, 'form' : ReplyForm(), 
                        })    
                else:
                    reply = form.save(commit=False)
                    # print('Reply:', reply, type(reply))
                    # 将接收到的表单数据(回复)绑定话题
                    reply.topic = topic
                    reply.author = self.request.user
                    # reply.picture = request.FILES['picture']
                    reply.save()
        except(KeyError):
            return render(self.request, 'bbs/detail.html', {'topic': topic, 'error_message': "传值出错！"})
        else:
            return HttpResponseRedirect(reverse('bbs:detail', args=(topic.id,)))

@login_required
def my_page(request):
    topic_list = Topic.objects.order_by('-pub_date').filter(author=request.user)

    form = TopicForm()
    context = {
        'topic_list': topic_list,
        'current_user':  {'user': request.user, 'is_login': request.user.is_authenticated},
        'from': form
    }
    
    return render(request, 'bbs/my_page.html', context)