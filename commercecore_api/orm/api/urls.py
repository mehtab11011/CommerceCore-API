
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register('user',user_view,basename="user")
router.register('custmer',custmer_view,basename="custmer")
router.register('product',product_view,basename="product")
router.register('order',order_view,basename="order")
router.register('orderitems',orderitems_view,basename="orderitems")




urlpatterns = [
    path("",include(router.urls))
    
]
