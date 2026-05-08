from django.urls import path
from .views import (
    BagListCreateView,
    BagDetailView,
    ScanArticleView,
    InvoiceArticleView,
    DispatchBagView
)

urlpatterns = [
    path('bags/', BagListCreateView.as_view()),
    path('bags/<str:bag_code>/', BagDetailView.as_view()),
    path('bags/<str:bag_code>/scan/', ScanArticleView.as_view()),
    path('articles/<int:pk>/invoice/', InvoiceArticleView.as_view()),
    path('bags/<str:bag_code>/dispatch/', DispatchBagView.as_view()),
]