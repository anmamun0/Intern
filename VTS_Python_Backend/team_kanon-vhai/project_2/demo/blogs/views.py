from django.views.generic import DetailView ,ListView
from django.shortcuts import get_object_or_404,redirect
from .models import Blog
from .utils import count_comments
from django.urls import reverse_lazy 
from django.views.generic import CreateView ,DeleteView
from .forms import BlogForm ,CommentForm 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        context["form"] = CommentForm()
        context["top_comments"] = blog.comments.filter(parent=None).order_by('-created_at')
        context["total_comments"] = blog.comments.count()
        return context

    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
        return redirect("blog_detail", pk=blog.pk)
 

class BlogListView(ListView):
    model = Blog
    template_name = "blogs_list.html"
    context_object_name = "blogs"
    ordering = ['-created_at'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        for blog in context['blogs']:
            blog.top_comments = blog.comments.filter(parent__isnull=True)
            blog.total_comments = count_comments(blog.top_comments)
        return context 

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add_blog.html'
    success_url = reverse_lazy('blogs_list')  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'  
    success_url = reverse_lazy('blog_detail')    
    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author
