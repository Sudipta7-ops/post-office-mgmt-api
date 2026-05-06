from rest_framework import generics
from .models import SpeedPostBooking
from .serializers import SpeedPostBookingSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsABPM, IsAdmin

class BookingListCreateView(generics.ListCreateAPIView):
    queryset= SpeedPostBooking.objects.all()
    serializer_class=SpeedPostBookingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article_number']

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpeedPostBooking.objects.all()
    serializer_class = SpeedPostBookingSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'article_number'
# Create your views here.
