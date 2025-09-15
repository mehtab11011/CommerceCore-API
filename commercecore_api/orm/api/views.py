from rest_framework import viewsets
from .searializers import *
from orm_app.models import *

class user_view(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class custmer_view(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    
class product_view(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
class order_view(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderItemSerializer
    
    
class orderitems_view(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
        