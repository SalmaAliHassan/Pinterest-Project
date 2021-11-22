from rest_framework import serializers
from pinterest.models import Pin,User
# from .serializers import PinSerializer




class PinSerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Pin
        # fields= ['id', 'title', 'alt_description', 'owner']
        fields ='__all__'


class UserSerializer(serializers.ModelSerializer):
    # pins= serializers.PrimaryKeyRelatedField(many=True, queryset=Pin.objects.all())
    pins=PinSerializer(many=True)
    followers= serializers.ReadOnlyField(source='followers.username')

    class Meta:
        model = User
        fields='__all__'
        # fields=['id','username','pins','followers']
