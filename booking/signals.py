from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SpeedPostBooking

@receiver(post_save, sender=SpeedPostBooking)
def booking_created_log(sender, instance, created, **kwargs):
    if created:
        print(f"[LOG] New booking created: {instance.article_number} at {instance.booked_at}")
        