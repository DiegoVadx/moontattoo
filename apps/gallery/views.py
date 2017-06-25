from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Image


class Gallery(TemplateView):
    template_name = 'vertical.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = Image.objects.filter(published=True).order_by('-id')
        return context