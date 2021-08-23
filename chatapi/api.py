import datetime

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Message
from rest_framework import permissions, mixins, status
from .serializers import MessageSerializer, MessageSerializerCustom


class MessageViewSetList(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Message.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MessageSerializer

    def retrieve(self, request, *args, **kwargs):
        number = int(kwargs['pk'])
        messages = Message.objects.all()[(number * 10):((number + 1) * 10)]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=200)


class MessageViewSetSingle(mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           GenericViewSet):
    queryset = Message.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MessageSerializerCustom

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_date'] = timezone.now()
        serializer.validated_data['update_date'] = serializer.validated_data['create_date']
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_date'] = timezone.now()
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

