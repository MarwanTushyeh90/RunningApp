
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import RunningSession

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='get_full_name', read_only=True)
    

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', )
   

        
class RunSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningSession
        fields = ('createdDate', 'name', 'miles', 'duration', )
   