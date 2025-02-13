from rest_framework import serializers
from .models import *

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = '__all__'

        # fields = ('title', 'seconds')

class BandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Band
        fields = '__all__'
    

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
