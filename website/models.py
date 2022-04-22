from django.db import models

# Create your models here.
from mongoengine import Document, StringField
import mongoengine

mongoengine.connect(db='ai_mark', host='localhost:27017')


class Probleme(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(max_length=100, null=False)
    desctiption = models.CharField(max_length=500, null=False)
    gravity = models.CharField(max_length=100, null=False)
    created_at = models.DateField(null=False)


class Probleme_image_xy(models.Model):
    Probleme_id = models.ForeignKey(Probleme, on_delete=models.CASCADE)
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
