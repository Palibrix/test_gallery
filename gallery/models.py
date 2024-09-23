from functools import reduce

from django.db import models
from django.utils.timezone import override


def upload_to_gallery(instance, filename):
    return f"images/{instance.gallery.__class__.__name__}/{filename}"


class Gallery(models.Model):
    gallery_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    def __str__(self):
        related_models = ['antenna', 'camera']  # Add more models here
        owner = next((getattr(self, model) for model in related_models if hasattr(self, model)), None)
        return f"{owner.__class__.__name__} {owner.id}" if owner else f"{self.__class__.__name__} {self.id}"

    @property
    def id(self):
        return self.gallery_id

class BasePartModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    class Meta:
        abstract = True


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to=upload_to_gallery)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        unique_together = ('gallery', 'order')


class Antenna(BasePartModel, Gallery):
    type = models.CharField(max_length=50, unique=True)


class Camera(BasePartModel, Gallery):
    name = None
    type = models.CharField(max_length=50, unique=True)

