from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, renderers
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from api.serializers import *
from marks.models import Mark


@api_view(['GET'])
def index(request):
    marks = Mark.objects.all()
    serialize = MarkSerializer(marks, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def specific(request,id):
    marks = Mark.objects.get(id=id)
    serialize = MarkSerializer(marks, many=False)
    return Response(serialize.data)

@api_view(['POST'])
def add(request):
    serialize = MarkSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)
    else:
        return Response(serialize.errors)



@api_view(['PUT'])
def edit(request,id):
    serialize = MarkSerializer(data=request.data,partial=True)
    if serialize.is_valid():
        # mark = Mark.objects.get(id=request.data['id'])
        serialize.save()

        return Response(serialize.data)
    else:
        return Response(serialize.errors)



@api_view(['DELETE'])
def delete(requestn,id):
    mark=Mark.objects.get(id=id)
    mark.delete()
    return Response('"statut": ["good"]')



@api_view(['GET'])
def search(request):
    marks = Mark.objects.filter(Q(name__contains=request.data['searchtext']) | Q(desctiption__contains=request.data['searchtext']))
    serialize = MarkSerializer(marks, many=True)
    return Response(serialize.data)






@api_view(['POST'])
def addpoint(request):
    serialize = PointsSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)
    else:
        return Response(serialize.errors)



@api_view(['DELETE'])
def deletepoint(requestn,id):
    point=Point.objects.filter(mark_id=id)
    point.delete()
    return Response('"statut": ["good"]')

#
# class MarkViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     serializer_class = MarkSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     # queryset = Mark.objects.all().select_related()
#
#     def perform_create(self, serializer):
#         serializer.save()
#         # return HttpResponse(serializer)
#
#     def get_queryset(self):
#         return Mark.objects.all()
#
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
#
#     # def list(self, request, *args, **kwargs):
#     #     queryset = self.get_queryset()
#     #     serializer = MarkSerializer(queryset, many=True)
#     #     return Response(serializer.data)
#     #
#
#
#     # def update(self, request, *args, **kwargs):
#     #     return super().update(request, *args, **kwargs)
#     #
#     # def destroy(self, request, *args, **kwargs):
#     #     return super().destroy(request, *args, **kwargs)
#

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
