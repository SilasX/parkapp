# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User

# Create your models here.


class ParkingSpot(models.Model):
    is_available = models.BooleanField(default=True)
    location = gis_models.PointField()

    def __unicode__(self):
        return unicode(self.location)


class Reservation(models.Model):
    user = models.ForeignKey(User)
    parking_spot = models.ForeignKey(ParkingSpot)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return "{0} : {1} : {2}".format(
            self.user.id,
            self.parking_spot,
            self.start_time,
        )
