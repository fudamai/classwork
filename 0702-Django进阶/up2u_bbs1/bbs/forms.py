from django import forms
from .models import Topic, Reply


class ReplyForm(forms.ModelForm):
    reply_text = forms.CharField(
        label= "你的回复",
        max_length=200,
        help_text='最大长度为200',
        widget = forms.TextInput(
            attrs={
                'placeholder':"水个贴吧",
                'class': 'form-control'
            }
        )
    )
    picture = forms.FileField(
        label= "添加图片（可选）",
        required=False,
        help_text='可以上传的格式：jpg、png。',
        widget = forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = Reply
        fields = ['reply_text', 'picture']


class TopicForm(forms.ModelForm):
    topic_text = forms.CharField(
        label= "发表新帖",
        max_length=200,
        help_text='最大长度为200',
        widget = forms.TextInput(
            attrs={
                'placeholder':"向社区分享吧",
                'class': 'form-control'
            }
        )
    )
    picture = forms.FileField(
        label= "添加图片（可选）",
        required=False,
        help_text='可以上传的格式：jpg、png。',
        widget = forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    topic_description = forms.CharField(
        label= "添加些内容",
        max_length=200,
        help_text='最大长度为2000',
        widget = forms.TextInput(
            attrs={
                'placeholder':"添加些内容",
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = Topic
        fields = ['topic_text', 'picture', 'topic_description']