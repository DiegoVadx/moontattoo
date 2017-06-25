from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'date', 'time', 'published']
    actions = ['show', 'hide']

    def show(self, request, queryset):
        queryset.update(published=True)

    def hide(self, request, queryset):
        queryset.update(published=False)

    show.short_description = 'Mark as show'
    hide.short_description = 'Mark as hide'