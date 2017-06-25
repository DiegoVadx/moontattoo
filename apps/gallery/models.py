from django.db import models

# Create your models here.


class Image(models.Model):
    url = models.URLField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
