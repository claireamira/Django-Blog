from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    context = {
        "posts" : Post.objects.all(),
    }
    return render(request, "blog_app/home.html", context)

#class PostListView(ListView):
 #   model = Post
  #  template_neme = "blog_app/home.html"
   # context_object_name = "posts"
def post_detail(request, pk):
    print(pk)
    post = Post.objects.filter(pk=pk).first()
    return render (request,  "blog_app/post_detail.html", {"post": post} )

def createPost(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("blog-home")  # Redirect to a page after successful creation
    else:
        form = PostCreateForm()

    return render(request, "blog_app/create_post.html", {'form': form})

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog_app/create_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog_app/create_post.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def myPosts(request):
    context = {
        "posts" : Post.objects.finter(author = request.uder).all()
    }
    return render(request, "blog_app/home.html", context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog_app/post_delete_confirm.html'
    success_url = "blog-home"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, "blog_app/about.html")

def contacts(request):
    return render(request, "blog_app/contacts.html")
