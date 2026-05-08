from django.db import models
from accounts.models import User
from booking.models import SpeedPostBooking


class Bag(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('dispatched', 'Dispatched'),
    ]
    bag_code = models.CharField(max_length=20, unique=True)
    bagging_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    received_at = models.DateTimeField(auto_now_add=True)
    dispatched_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.bag_code


class DeliveryArticle(models.Model):
    STATUS_CHOICES = [
        ('scanned', 'Scanned'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('undelivered', 'Undelivered'),
        ('deposited', 'Deposited'),
    ]
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, related_name='articles')
    article = models.ForeignKey(SpeedPostBooking, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scanned')
    scanned_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    delivery_boy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='deliveries')

    def __str__(self):
        return f"{self.article.article_number} - {self.status}"

# Create your models here.
