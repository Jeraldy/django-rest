from django.conf.urls import url
from . import views

urlpatterns = [
    url('products/', views.product_list),
]