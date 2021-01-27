from . import views
from  django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
     path('<slug:category_slug>', views.home, name='product_by_category'),
     path('<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
]