from rest_framework import generics
from .models import SpeedPostBooking
from .serializers import SpeedPostBookingSerializer
from rest_framework.permissions import IsAuthenticated

class BookingListCreateView(generics.ListCreateAPIView):
    queryset= SpeedPostBooking.objects.all()
    serializer_class=SpeedPostBookingSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
