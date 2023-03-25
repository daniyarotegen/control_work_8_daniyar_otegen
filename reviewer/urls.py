from django.urls import path
from .views import IndexView, ProductCreateView, ProductDetail, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]
