from rest_framework import serializers
from .models import Set_Location



class Set_LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set_Location
        fields = ('name', 'description', 'price', 'image')