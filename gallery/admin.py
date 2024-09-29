from django.contrib import admin
from django.utils.html import format_html

from .models import Antenna, Camera, Image, Gallery

# admin.site.register(Gallery)

class ImageInline(admin.StackedInline):
    model = Image
    min_num = 1
    extra = 0


# @admin.register(BasePartModel)
# class BasePartModelAdmin(admin.ModelAdmin):
#     list_display = ('id', '__str__')

@admin.register(Antenna)
class AntennaAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'name', 'type')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', '__str__')

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'type')

# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'part', 'created_at')
#     readonly_fields = ('created_at',)

# @admin.register(PartImage)
# class ImageFileAdmin(admin.ModelAdmin):
#     # def image_tag(self, obj):
#     #     return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.file.url))
#     #
#     # image_tag.short_description = 'Image'
#     list_display = ['part', 'image', 'order']

