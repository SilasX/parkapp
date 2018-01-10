# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from serializers import UserSerializer, GroupSerializer
from rest_framework.serializers import ModelSerializer
from models import ParkingSpot


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
        return queryset
