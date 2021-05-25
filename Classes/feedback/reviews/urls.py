from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankyouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    #Using int:pk with DetailView, django searchs for the specific register
    path("review/<int:pk>", views.SingleReviewView.as_view())
]