from datetime import datetime
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer
 

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer
    
class UpdatingBooking(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
    
    
class DeleteBooking(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'