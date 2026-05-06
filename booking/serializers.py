from rest_framework import serializers
from .models import SpeedPostBooking
import re

class SpeedPostBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpeedPostBooking
        fields = '__all__'
        read_only_fields = ['booked_at']

    def validate_article_number(self, value):
        pattern = r'^[A-Z]{2}[0-9]{9}[A-Z]{2}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Article number must be in format like EE123456789IN"
            )
        return value

    def validate_weight_grams(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Weight must be greater than 0"
            )
        return value