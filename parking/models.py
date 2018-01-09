# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.


class ParkingSpot(models.Model):
    is_available = models.BooleanField(default=True)
    location = gis_models.PointField()

    def __unicode__(self):
        return unicode(self.location)
