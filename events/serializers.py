from . import models
from EventAPI import settings
from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import GEOSGeometry, LineString, Point, Polygon


class EventSerializer(geo_serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Event
        geo_field = "location"
        fields = ('id', 'name', 'time', 'description', 'location', 'owner')



class AttendeesSerializer(geo_serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Attendees
        geo_field = ""
        fields = ('id', 'attendee', 'event')
