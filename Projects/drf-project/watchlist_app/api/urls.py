from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, 
                                     StreamPlatformListAV, StreamPlatformDetailAV, StreamPlatformVS,
                                     ReviewList, ReviewDetail, ReviewCreate)
#Function views
# from watchlist_app.api.views import movie_list, movie_detail

# urlpatterns = [
#     path('list/', movie_list, name='move-list'),
#     path('<int:pk>', movie_detail, name='move-detail'),
# ]

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplataform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-detail'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

]
