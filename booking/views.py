from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import SpeedPostBooking
from .serializers import SpeedPostBookingSerializer
from .permissions import IsABPM, IsAdmin

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = SpeedPostBooking.objects.all()
    serializer_class = SpeedPostBookingSerializer
    permission_classes = [IsABPM]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['article_number']
    search_fields = ['article_number']
    ordering_fields = ['booked_at', 'weight_grams']
    ordering = ['-booked_at']

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpeedPostBooking.objects.all()
    serializer_class = SpeedPostBookingSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'article_number'

