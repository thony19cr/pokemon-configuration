
# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Catalogo(models.Model):
    nombre_catalogo = models.CharField(max_length=40)
    especie = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    dia_creacion = models.DateTimeField(default=timezone.now())


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
