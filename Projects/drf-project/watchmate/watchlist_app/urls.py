from django.urls import path, include
from watchlist_app.views import movie_list, movie_detail

urlpatterns = [
    path('list/', movie_list, name='move-list'),
    path('<int:pk>', movie_detail, name='move-detail'),
]
