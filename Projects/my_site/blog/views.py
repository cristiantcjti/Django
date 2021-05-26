from django.db.models import query
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Comment, Post
from .forms import CommentForm

# Create your views here.


#OOP solution
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# Functional solution
"""
def starting_page(request):
    latest_posts = Post.objects.filter().order_by("-date")[:3] # [:3] it is possible to slice a queryset but only positivelly.
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })
"""
#########################################################
#OOP solution
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts" 

# Functional solution
"""
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })
"""



#########################################################
#OOP solution
class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post 

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

# Functional solution
"""
def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all() # It goes to the related model and gets the information required.
    })
"""