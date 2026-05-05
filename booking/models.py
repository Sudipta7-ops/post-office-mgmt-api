from django.db import models

# Create your models here.
class SpeedPostBooking(models.Model):
    article_number=models.CharField(max_length=50, unique=True)
    weight_grams=models.PositiveIntegerField()
    booked_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_number

