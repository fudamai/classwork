from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label= "标题",
        max_length = 100,
        help_text = "最大长度为100",
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'required':'True',
            },
        )
    )
    content = forms.CharField(
        label = "描述",
        max_length = 500,
        help_text = "最大长度为500",
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'required':'True',
            },
        )
    )
    important = forms.CharField(
        label = "优先级",
        widget = forms.Select(
            attrs = {
                'class':'form-control',
                'required':'True',
            },
            choices = Todo.IMPORTANT_CHOICE,
        )
    )
    duedate = forms.DateField(
        label = "执行时间",
        widget = forms.SelectDateWidget(
            attrs = {
                'class':'col-3',
            },
        )
    )

    class Meta:
        model = Todo
        fields = ['title', 'content', 'important', 'duedate']

class TodoModifiForm(forms.ModelForm):
    title = forms.CharField(
        label= "标题",
        max_length = 100,
        help_text = "最大长度为100",
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'required':'True',
            },
        )
    )
    content = forms.CharField(
        label = "描述",
        max_length = 500,
        help_text = "最大长度为500",
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'required':'True',
            },
        )
    )

    class Meta:
        model = Todo
        fields = ['title', 'content',]