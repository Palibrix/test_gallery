from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import AntennaForm, ImageInlineFormset
from .models import Antenna, Camera

class AntennaListView(ListView):
    model = Antenna
    template_name = 'antennas_list.html'
    context_object_name = 'antennas'

class CameraListView(ListView):
    model = Camera
    template_name = 'cameras_list.html'
    context_object_name = 'cameras'


class AntennaCreateView(CreateView):
    form_class = AntennaForm
    success_url = 'list'
    template_name = 'gallery/antenna_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['images'] = ImageInlineFormset(self.request.POST, self.request.FILES)
        else:
            context['images'] = ImageInlineFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        if images.is_valid():
            self.object = form.save()
            images.instance = self.object.gallery_ptr
            images.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class AntennaUpdateView(UpdateView):
    model = Antenna
    form_class = AntennaForm
    success_url = 'update_antenna'
    template_name = 'gallery/antenna_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['images'] = ImageInlineFormset(self.request.POST, self.request.FILES)
        else:
            context['images'] = ImageInlineFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        if images.is_valid():
            self.object = form.save()
            images.instance = self.object.gallery_ptr
            images.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
