from rest_framework import serializers
from .models import *

class directorserializer(serializers.ModelSerializer):
    class Meta:
        model=director
        fields=['name']

class movieserializer(serializers.ModelSerializer):
    #director_name = serializers.RelatedField(source='director',read_only=False)
    #director_name=directorserializer(read_only=True, many=True)
    director=serializers.StringRelatedField()
    actors=serializers.StringRelatedField(many=True)
    class Meta:
        model=movie
        fields=['name','release_date','genre','director','actors']



class leadactorsserializer(serializers.ModelSerializer):
    class Meta:
        model=leadactors
        fields=['name']
