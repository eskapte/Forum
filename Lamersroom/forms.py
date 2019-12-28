from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import Select, HiddenInput, Textarea, Input
from .models import Post, Comment


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Уникальное имя пользователя',
            'email': 'Адрес эл.почты',
        }


class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'rubric', 'author')
        labels = {
            'title': 'Заголовок поста',
            'text': 'Опишите вашу проблему',
            'rubric': 'Выберите тему вашего поста',
        }
        widgets = {
            'rubric': Select(),
            'author': HiddenInput(),
            'title': Input(attrs={'class': 'add-title'}),
            'text': Textarea(attrs={'class': 'add-text'})
        }


class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'comment_author', 'post')
        widgets = {
            'comment_author': HiddenInput(),
            'content': Textarea(attrs={'rows': 6, 'cols': 50, 'placeholder': 'Введите комментарий ...'}),
            'post': HiddenInput()
        }


class UpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('status', 'close_time')
        widgets = {
            'status': HiddenInput(),
            'close_time': HiddenInput(),
        }