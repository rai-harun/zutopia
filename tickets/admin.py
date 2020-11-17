from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(VehicleRouteFrom)
admin.site.register(VehicleRouteTo)
admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(AvailableTickets)
admin.site.register(TicketDetails)