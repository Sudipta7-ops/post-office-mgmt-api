from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Bag, DeliveryArticle
from .serializers import BagSerializer, DeliveryArticleSerializer
from booking.permissions import IsABPM, IsAdmin


class BagListCreateView(generics.ListCreateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    permission_classes = [IsABPM]

    def perform_create(self, serializer):
        serializer.save(received_by=self.request.user)


class BagDetailView(generics.RetrieveUpdateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
    permission_classes = [IsABPM]
    lookup_field = 'bag_code'


class ScanArticleView(APIView):
    permission_classes = [IsABPM]

    def post(self, request, bag_code):
        try:
            bag = Bag.objects.get(bag_code=bag_code)
        except Bag.DoesNotExist:
            return Response({'error': 'Bag not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeliveryArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(bag=bag, delivery_boy=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceArticleView(APIView):
    permission_classes = [IsABPM]

    def patch(self, request, pk):
        try:
            article = DeliveryArticle.objects.get(pk=pk)
        except DeliveryArticle.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get('status')
        if new_status in ['delivered', 'undelivered', 'deposited']:
            article.status = new_status
            if new_status == 'delivered':
                article.delivered_at = timezone.now()
            article.save()
            return Response(DeliveryArticleSerializer(article).data)
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)


class DispatchBagView(APIView):
    permission_classes = [IsABPM]

    def patch(self, request, bag_code):
        try:
            bag = Bag.objects.get(bag_code=bag_code)
        except Bag.DoesNotExist:
            return Response({'error': 'Bag not found'}, status=status.HTTP_404_NOT_FOUND)

        bag.status = 'dispatched'
        bag.dispatched_at = timezone.now()
        bag.save()
        return Response(BagSerializer(bag).data)

# Create your views here.
