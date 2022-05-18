import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from marks.models import Mark, Point


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PointsSerializer(serializers.ModelSerializer):
    mark_id=serializers.IntegerField()
    class Meta:
        model = Point
        fields = ['mark_id', 'num', 'x', 'y']


class MarkSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    points = PointsSerializer(many=True, read_only=True, required=False)
    image = serializers.CharField()
    created_at = serializers.DateField(default=datetime.date.today())

    class Meta:
        model = Mark
        fields = ['id', 'user', 'points', 'name', 'image', 'desctiption', 'descx', 'descy', 'gravity',
                  'created_at']
