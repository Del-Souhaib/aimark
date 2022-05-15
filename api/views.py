from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from httplib2 import Response
from rest_framework import viewsets, permissions, generics, renderers
from rest_framework.decorators import action

from api.serializers import *
from marks.models import Mark


class MarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = MarkSerializer
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Mark.objects.all().select_related()

    def perform_create(self, serializer):
        serializer.save()
        # return HttpResponse(serializer)

    def get_queryset(self):
        return Mark.objects.all()

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = MarkSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #


    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
