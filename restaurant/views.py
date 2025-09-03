from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking


# Create your views here.
def index(request):
    return render(request, 'index.html', {})
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemVIew(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

    