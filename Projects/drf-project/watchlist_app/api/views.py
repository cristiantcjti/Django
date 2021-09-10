from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchList, StreamPlatformSerializer

class StreamPlatformListAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListAV(APIView):

    def get(self, request, *args, **kwargs):
        movies = WatchList.objects.all()
        serializer = WatchList(movies, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = WatchList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    
    def get(self, request, pk: str)-> dict:
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchList(movie)
        return Response(serializer.data)

    def put(self, request, pk: str)-> dict:
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchList(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: str):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Function views 

# @api_view(['GET', 'POST'])
# def movie_list(request)-> dict:
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = WatchList(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = WatchList(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk: str)-> dict:    
#     if request.method == 'GET':
        
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = WatchList(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = WatchList(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
