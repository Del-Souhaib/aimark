from django.contrib.auth.models import User
from rest_framework import serializers

from marks.models import Mark, Point


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['id','num', 'x', 'y']


class MarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=False)
    points = PointsSerializer(many=True, read_only=False)

    class Meta:
        model = Mark
        fields = ['url', 'user','points', 'name', 'image', 'desctiption', 'descx', 'descy', 'gravity',
                  'created_at']
