from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="post-page"),
    # slug is acctualy a concept of route like = /posts/my-first-post where we can include symbols.
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]
