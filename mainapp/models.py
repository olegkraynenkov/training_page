from django.db import models


class Picture(models.Model):
    image = models.ImageField(upload_to='gallery_image')
    comment = models.TextField(blank=True)
