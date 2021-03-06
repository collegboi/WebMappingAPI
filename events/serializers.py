from . import models
from EventAPI import settings
from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers
from rest_framework_gis import serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import GEOSGeometry, LineString, Point, Polygon


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class EventSerializer(geo_serializers.GeoFeatureModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = models.Event
        geo_field = "location"
        fields = ('id', 'name', 'time', 'description', 'location', 'owner')


class AttendeesSerializer(serializers.ModelSerializer):
    attendee = UserSerializer(read_only=True)

    class Meta:
        model = models.Attendees
        fields = ('id', 'attendee', 'event')


class UpdateAttendeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Attendees
        fields = ('attendee', 'event')


class UpdateEventSerializer(geo_serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Event
        geo_field = "location"
        fields = ('name', 'time', 'description', 'location', 'owner')

