from rest_framework import generics
from .models import SpeedPostBooking
from .serializers import SpeedPostBookingSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class BookingListCreateView(generics.ListCreateAPIView):
    queryset= SpeedPostBooking.objects.all()
    serializer_class=SpeedPostBookingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article_number']
# Create your views here.
