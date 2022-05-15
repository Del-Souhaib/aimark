from rest_framework import serializers

from marks.models import Mark


class MarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mark
        fields = ['url',  'name', 'image', 'desctiption', 'descx', 'descy', 'gravity',
                  'created_at']
