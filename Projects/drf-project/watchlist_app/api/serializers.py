from django.utils.translation import activate
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class WatchSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchSerializer(many=True, read_only=True) # Ruturn all data
    #watchlist = serializers.StringRelatedField(many=True, read_only=True) # Return only the title
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # Return the primary key
    #watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True, 
    #     view_name="movie-detail" 
    #     ) # Return a link to the movie

    class Meta:
        model = StreamPlatform
        fields = "__all__"

#####################################
#### serializers.ModelSerializer ####
#####################################
'''
class WatchSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"

    def get_len_name(self, obj: WatchList):
        return len(obj.name)

    #Object validation
    def validate(self, data: dict)-> dict:
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description should be different")
        return data        

    #Field validation
    def validate_name(self, value: str)-> dict:
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value
'''
################################
#### serializers.Serializer ####
################################
"""
#Validators[]
def name_length(value):
    if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")

class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    name = serializers.CharField(validators=[name_length]) #Validators[]
    description = serializers.CharField()
    active = serializers.BooleanField()

    #POST
    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)

    #PUT
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    #Object validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description should be different")
        return data         

    #Field validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value
"""