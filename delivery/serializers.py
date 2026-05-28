from rest_framework import serializers
from .models import Bag, DeliveryArticle


class DeliveryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryArticle
        fields = '__all__'
        read_only_fields = ['scanned_at', 'delivery_boy','bag']


class BagSerializer(serializers.ModelSerializer):
    articles = DeliveryArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Bag
        fields = '__all__'
        read_only_fields = ['received_at', 'received_by']