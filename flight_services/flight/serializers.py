from rest_framework import serializers

from flight.models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    """Serializer for a Flight model"""
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    """Serializer for a Passenger model"""
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    """Serializer for a Reservation model"""
    class Meta:
        model = Reservation
        fields = '__all__'