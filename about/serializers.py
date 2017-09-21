from rest_framework import serializers
from .models import Abou



class AbouSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Abou
        fields = ('name', 'description', 'price', 'image')