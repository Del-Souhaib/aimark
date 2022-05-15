from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from api.serializers import MarkSerializer
from marks.models import Mark


class MarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mark.objects.all().order_by('-created_at')
    serializer_class = MarkSerializer
    permission_classes = [permissions.AllowAny]
