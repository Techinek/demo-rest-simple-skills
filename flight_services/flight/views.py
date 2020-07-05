from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from flight.models import Flight, Passenger, Reservation
from flight.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


@api_view(['POST'])
def find_flights(request):
    """function that finds flights by custom filters"""
    flights = Flight.objects.filter(
        departure_city=request.data['departure_city'],
        arrival_city=request.data['arrival_city'],
        date_of_departure=request.data['date_of_departure'],
    )
    serializer=FlightSerializer(flights, many=True)
    return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
    """View for rendering Flight model"""
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    """View for rendering Passenger model"""
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """View for rendering Reservation model"""
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer