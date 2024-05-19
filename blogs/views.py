from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('blogs:home')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Foydalanuvchini avtor sifatida o'rnating
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse_lazy('blogs:post_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogs:home')


class BlogSortMyBlogsView(View):
    template_name = 'my_blogs.html'

    def get(self, request, *args, **kwargs):
        my_blogs = Post.objects.filter(author=request.user)
        context = {
            'my_blogs': my_blogs,
            'title': 'My Blogs',
        }
        return render(request, self.template_name, context)