from django.db import models


class Flight(models.Model):
    """Class for flight information"""
    flight_number = models.CharField(max_length=10)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return self.flight_number


class Passenger(models.Model):
    """Class for passenger information"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name


class Reservation(models.Model):
    """Reservation model with one-to-one relationships with passenger and flight models"""
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
