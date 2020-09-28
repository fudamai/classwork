from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Reply, Topic

# 使用基于类的通用视图实现

class IndexView(generic.ListView):
    template_name = 'bbs/index.html'
    # 定义上下文的键名
    context_object_name = 'topic_list'

    # 可以很方便地使用 get_queryset 来给查询集添加逻辑
    def get_queryset(self):
        """Return Topics."""
        return Topic.objects.order_by('-pub_date')

    # 定义函数，操作帖子（topic）添加
    def post(self, request, *args, **kwargs):
        try:
            name = request.POST['topic_author']
            text = request.POST['topic_text']
            print(name, text)
            if name and text:
                t = Topic(author=name, topic_text=text)
                t.save()
            else:
                return render(request, 'bbs/index.html', {'topic_list': Topic.objects.all(), 'error_message': "请勿输入空值！"})
        except(KeyError):
            return render(request, 'bbs/index.html', {'topic_list': Topic.objects.all(), 'error_message': "传值出错！"})
        else:
            return HttpResponseRedirect(reverse('bbs:index',))


class DetailView(generic.DetailView):
    # 指定 model = Publisher 只是 queryset = Publisher.objects.all() 的简写
    model = Topic
    template_name = 'bbs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 往上下文中添加一个topic_list
        # topic = get_object_or_404(Topic, pk=pk)
        # list = topic.reply_set.filter(reply_set__count > 5)
        context['topic_list'] = Topic.objects.all()
        return context

    def post(self, request, pk, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=pk)
        try:
            name = request.POST['reply_name']
            text = request.POST['reply_text']
            print(pk, name, text)
            if name and text:

                topic.reply_set.create(reply_text=text, author=name)
            else:
                return render(request, 'bbs/detail.html', {'topic': topic, 'error_message': "请勿输入空值！"})
        except(KeyError):
            return render(request, 'bbs/detail.html', {'topic': topic, 'error_message': "传值出错！"})
        else:
            return HttpResponseRedirect(reverse('bbs:detail', args=(topic.id,)))