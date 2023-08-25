from .models import *
from rest_framework import serializers

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['first_name','last_name','email','password']
        
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
