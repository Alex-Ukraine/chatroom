import re

from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageSerializerCustom(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['email', 'text']

    def validate(self, data):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, data['email'])):
            raise serializers.ValidationError("not valid email")
        return data
