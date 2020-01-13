from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Rubric, Comment
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.base import RedirectView
from .forms import RegisterUserForm, AddPost, AddComment, UpdateForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from django_ajax.mixin import AJAXMixin
from django.shortcuts import HttpResponse

def index(request):
    posts = Post.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(posts, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'posts': page.object_list, 'rubrics': rubrics, 'page': page}
    return render(
        request,
        'Lamersroom/index.html',
        context
    )


class DetailPost(DetailView, FormView):
    model = Post
    template_name = 'Lamersroom/detail.html'
    form_class = AddComment

    
    def post(self, request, **args):
        self.object = self.get_object()

        if self.request.is_ajax():
            like_id = self.request.POST.get("id")
            liked_comment = Comment.objects.get(pk=like_id)
            current_user = self.request.user
            if current_user in liked_comment.likes.all():
                liked_comment.likes.remove(current_user.pk)
                return HttpResponse('like-removed')
            else:
                liked_comment.likes.add(current_user.pk)
                return HttpResponse('like-added')

        return super().post(request, **args)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=context['post'].pk)
        context['form'] = self.get_form()
        return context

    def get_initial(self):
        self.initial = super().get_initial()
        self.initial['comment_author'] = self.request.user.pk
        self.initial['post'] = self.get_object().pk
        return self.initial

    def get_success_url(self):
        url = '/%s' % self.get_object().pk
        return url

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ClosePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'Lamersroom/close_post.html'
    initial = {'status': 'c', 'close_time': timezone.now()}

    def get_success_url(self):
        url = '/%s' % self.get_object().pk
        return url

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserRegister(CreateView):
    template_name = 'Lamersroom/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')



class UserLogin(LoginView):
    template_name = 'Lamersroom/login.html'

    def get_redirect_url(self):
        self.next = super().get_redirect_url()
        if self.next:
            return self.next
        self.next = '/'
        return self.next


def user_profile(request, username):
    user = User.objects.get(username=username)
    context = {'c_user': user}
    return render(
        request,
        'Lamersroom/profile.html',
        context
    )


class AddNewPost(CreateView):
    template_name = 'Lamersroom/create.html'
    form_class = AddPost
    success_url = '/{id}'

    def get_initial(self):
        self.initial = super().get_initial()
        self.initial['author'] = self.request.user.pk
        return self.initial


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    template_name_suffix = '_delete'