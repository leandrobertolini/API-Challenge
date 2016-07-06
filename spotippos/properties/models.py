from __future__ import unicode_literals

from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    bed = models.IntegerField(blank=False)
    bath = models.IntegerField(blank=False)
    price = models.DecimalField(blank=False, decimal_places=2, max_digits=10)
    squareMeters = models.IntegerField(blank=False)
    cordinate_x = models.IntegerField(blank=False)
    cordinate_y = models.IntegerField(blank=False)
    provinces = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
