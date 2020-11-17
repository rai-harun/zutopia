from django.urls import path
from . import views


urlpatterns = [
    path('', views.ticketsHome, name="ticketshome"),
    path('nightbusdetails/', views.NightBusDetails, name="nightbusdetails"),
    path('busdetails/<int:pk>/', views.BusDetails, name="busdetails"),
    path('busdetails/<int:pk>/bookticket', views.BookTicket, name="bookticket"),
    path('ticketdetails/<int:pk>/', views.BusTicketDetails, name="ticketdetails"),
    path('paymentverify/', views.verify_payment, name="payment_verify")
]



