from rest_framework import serializers
from .models import SpeedPostBooking

class SpeedPostBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model= SpeedPostBooking
        fields="__all__"