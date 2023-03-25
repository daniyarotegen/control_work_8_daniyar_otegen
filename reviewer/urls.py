from django.urls import path
from reviewer.views.product import ProductCreateView, ProductDetail, ProductDeleteView, ProductUpdateView, \
    ProductListView
from reviewer.views.review import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/add_review/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
