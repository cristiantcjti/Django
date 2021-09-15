from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewList, ReviewDetail
#Function views
# from watchlist_app.api.views import movie_list, movie_detail

# urlpatterns = [
#     path('list/', movie_list, name='move-list'),
#     path('<int:pk>', movie_detail, name='move-detail'),
# ]

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('stream/<int:pk>/review/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    # path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

]
