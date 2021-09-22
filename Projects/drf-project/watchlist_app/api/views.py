from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist ,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this program.")

        if watchlist.avg_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2

        watchlist.number_rating += 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewList(generics.ListAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  
    permission_classes = [ReviewUserOrReadOnly]  


######################
#### Using Mixins ####
######################
'''
class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''

#######################################
#### Function viewset.ModelViewset ####
####  GET, POST, PUT, PATCH,DELETE ####
#######################################

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

# class StreamPlatformVS(viewsets.ReadOnlyModelViewSet):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer


##################################
#### Function viewset.Viewset ####
##################################
'''
class StreamPlatformVS(viewsets.ViewSet):
    
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)

    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
'''

class StreamPlatformListAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        # serializer = StreamPlatformSerializer(platform, many=True, context={'request': request}) # To hyperlinkseriali
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk: str) -> dict:
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk: str) -> dict:
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: str) -> None:
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request, *args, **kwargs):
        movies = WatchList.objects.all()
        serializer = WatchSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self, request, pk: str) -> dict:
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk: str) -> dict:
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: str):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########################
#### Function views ####
########################
'''

@api_view(['GET', 'POST'])
def movie_list(request)-> dict:
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = WatchList(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = WatchList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk: str)-> dict:
    if request.method == 'GET':

        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchList(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = WatchList(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''