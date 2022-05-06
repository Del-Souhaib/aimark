
# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Mark(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(max_length=100, null=False)
    desctiption = models.CharField(max_length=500, null=False)
    gravity = models.IntegerField(null=False)
    created_at = models.DateField(null=False)


class Mark_x_y(models.Model):
    probleme = models.ForeignKey(Mark, on_delete=models.CASCADE)
    num = models.IntegerField(null=False,default=1)
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
