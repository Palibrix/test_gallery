from django import forms
from django.forms import inlineformset_factory

from .models import Antenna, Camera, Image


class AntennaForm(forms.ModelForm):
    class Meta:
        model = Antenna
        exclude = ()

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        exclude = ()


ImageInlineFormset = forms.inlineformset_factory(Antenna, Image, fields='__all__', min_num=1, extra=10, max_num=10)
