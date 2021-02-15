from django.db import models

# Create your models here.
class VehicleType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class VehicleRouteFrom(models.Model):
    routefrom = models.CharField(max_length=200, default=None)
    
    def __str__(self):
        return self.routefrom

class VehicleRouteTo(models.Model):
    routeto = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.routeto

class Vehicle(models.Model):
    vnumber = models.CharField(max_length=100)
    vname = models.CharField(max_length=200)
    vtype = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vseat = models.IntegerField()
    vroutefrom = models.ForeignKey(VehicleRouteFrom, on_delete=models.CASCADE, default=None)
    vrouteto = models.ForeignKey(VehicleRouteTo, on_delete=models.CASCADE, default=None)
    vimage = models.ImageField(blank=True, upload_to='images')
    vdescription = models.TextField(blank=True)

    def __str__(self):
        return self.vnumber + self.vname

class AvailableTickets(models.Model):
    seats = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
        ('A7', 'A7'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B4', 'B4'),
        ('B5', 'B5'),
        ('B6', 'B6'),
        ('B7', 'B7'),
    )
    vnumber = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vtickets = models.CharField(max_length=100, choices=seats)

    def __str__(self):
        return str(self.vnumber)+' ' + self.vtickets

class TicketDetails(models.Model):
    vtickets = models.ForeignKey(AvailableTickets, on_delete=models.CASCADE)
    vdeparttime = models.DateTimeField(verbose_name='related date time')
    vticketprice = models.FloatField()

    def __str__(self):
        return str(self.vticketprice)
