from django.urls import path
from .views import BookingListCreateView, BookingDetailView

urlpatterns = [
    path('bookings/', BookingListCreateView.as_view()),
    path('bookings/<str:article_number>/', BookingDetailView.as_view()),
]