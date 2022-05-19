
# Create your models here.
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.templatetags.static import static
from django.utils.datetime_safe import datetime

fs=FileSystemStorage(location='/marks')

class Mark(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="marks")
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(max_length=100, null=False,upload_to='marks/')
    desctiption = models.CharField(max_length=500, null=False)
    descx = models.FloatField(null=False)
    descy = models.FloatField(null=False)
    gravity = models.IntegerField(null=False)
    created_at = models.DateField(default=datetime.now,null=False)

    def __str__(self):
        return self.name


class Point(models.Model):
    mark = models.ForeignKey(Mark,related_name='points', on_delete=models.CASCADE)
    num = models.IntegerField(null=False,default=1)
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
