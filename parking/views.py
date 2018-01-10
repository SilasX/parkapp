# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from serializers import UserSerializer, GroupSerializer
from rest_framework.serializers import ModelSerializer
from models import ParkingSpot

from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ParkingSpotListSerializer(ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ('id', 'is_available', 'location')


class ParkingSpotList(generics.ListCreateAPIView):

    serializer_class = ParkingSpotListSerializer
    # model = ParkingSpot

    def get_queryset(self):
        queryset = ParkingSpot.objects.all()
        near = self.request.query_params.get('near')
        distance = self.request.query_params.get('distance')
        if near:
            # user has specified a near parameter, looking for
            # objects within a certain distance; assume distance
            # is in km
            try:
                point = fromstr(near, srid=4326)
                if distance:
                    try:
                        distance = float(distance)
                    except ValueError:
                        # Default to 2 km.
                        distance = 2
                else:
                    distance = 2
                queryset = queryset.filter(
                    location__distance_lte=(point, D(km=distance))
                )
            except ValueError:
                # Ignore all the above and just return queryset
                return queryset
        return queryset
