from django.urls import path
from products.views import home_view,product_detail_view,product_create_view

app_name='products'
urlpatterns = [
    path('',home_view,name='home'),
    path('detail/<int:my_id>/',product_detail_view,name='product_detail'),
    path('create/',product_create_view,name='product_create'),
   
]
