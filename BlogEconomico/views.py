from django.shortcuts import render
from BlogEconomico.models import Blog
from BlogEconomico.forms import BlogForm
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, "BlogEconomico/index.html")

class BlogList(ListView):
    model = Blog
    context_object_name = "blogs"

class BlogMineList(LoginRequiredMixin, BlogList):

    def get_queryset(self):
        return Blog.objects.filter(publisher=self.request.user.id).all()


class BlogDetail(DetailView):
    model = Blog
    context_object_name = "blog"

class OwnerPermissions(UserPassesTestMixin):

    def test_func(self):
        user_id = self.request.user.id
        blog_id = self.kwargs.get("pk")
        return Blog.objects.filter(publisher=user_id, id=blog_id).exists()

class BlogUpdate(LoginRequiredMixin, OwnerPermissions, UpdateView):
    model = Blog
    success_url = reverse_lazy("blog-list")
    fields = '__all__'

class BlogDelete(LoginRequiredMixin, OwnerPermissions, DeleteView):
    model = Blog
    context_object_name = "blog"
    success_url = reverse_lazy("blog-list")

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy("blog-list")
    fields = '__all__'

class BlogSearch(ListView):
    model = Blog
    context_object_name = "blogs"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Blog.objects.filter(title__icontains=criterio).all()
        return result
    
class Login(LoginView):
    next_page = reverse_lazy("blog-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('blog-list')

class Logout(LogoutView):
    template_name = "registration/logout.html"


    


   



