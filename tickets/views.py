from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import requests
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def ticketsHome(request):
    return HttpResponse('Tickets Home Page')
import requests
def NightBusDetails(request):
    totalVehicle = Vehicle.objects.all()
    print(totalVehicle)
    context = {
        'vehicles': totalVehicle
    }
    return render(request, 'nightbusdetails.html', context)

def BusDetails(request, pk):
    busDetails = Vehicle.objects.get(id=pk)
    context = {
        'busdetails': busDetails
    }
    return render(request, 'busdetails.html', context)

def BookTicket(request, pk):
    busDetailsImage = Vehicle.objects.get(id=pk)
    busDetails = AvailableTickets.objects.get(id=pk)
    context = {
        'busdetails': busDetails,
        'busDetailsImage': busDetailsImage
    }
    return render(request, 'bookticket.html', context)

def BusTicketDetails(request, pk):
    ticketDetails = TicketDetails.objects.get(id=pk)
    busDetailsImage = Vehicle.objects.get(id=pk)
    context = {
        'ticketDetails': ticketDetails,
        'busDetailsImage': busDetailsImage
    }
    return render(request, 'ticketdetails.html', context)

@csrf_exempt
def verify_payment(request):
    data = request.POST
    token = data['token']
    amount = data['amount']
    product_name = ['product_name']

    print(token, amount, product_name)
    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
    "token": token,
    "amount": amount
    }
    headers = {
    "Authorization": "Key test_secret_key_9c9cc66a17c04144bd225fceb3c85d97"
    }

    response = requests.post(url, payload, headers = headers)
    print(response)

    response_data = json.loads(response.text)
    status_code = str(response.status_code)
    if status_code == '400':
        response = JsonResponse({
            'status': 'false',
            'message': response_data['detail']                
        }, status = 500
        )
        return response
    
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response_data)

    return JsonResponse(f"Payment completed with idx {response_data['user']['idx']}", safe=False)

def transaction(request):
    url = "https://khalti.com/api/v2/merchant-transaction/"
    payload = {}
    headers = {
    "Authorization": "Key test_secret_key_9c9cc66a17c04144bd225fceb3c85d97"
    }

    response = requests.get(url, payload, headers = headers)
    data = response.json()
    # filtered_data = data['total_pages']
    # print(type(data))
    # print(data)
    filtered_data = data['records']
    
    # for i in filtered_data:
    #     transaction_idx = i['idx']
    #     transaction_type = i['type']['name']
    #     transaction_state = i['state']['name']
    #     transaction_amount = i['amount']
    #     transaction_fee_amount = i['fee_amount']
    #     transaction_refunded = i['refunded']
    #     transaction_created_on = i['created_on']
    #     transaction_user_name = i['user']['name']
    #     transaction_user_phone = i['user']['mobile']
    #     transaction_user_email = i['user']['email']

    #     print(transaction_user_name)


    context = {
        'res': filtered_data,
        # 'transaction_idx': transaction_idx,
    }
    return render(request, 'transaction.html', context)

def transaction_detail(request, idx):
    url = "https://khalti.com/api/v2/merchant-transaction/"+idx
    headers = {
    "Authorization": "Key test_secret_key_9c9cc66a17c04144bd225fceb3c85d97"
    }

    response = requests.get(url, headers = headers)
    res = response.json()
    # print(res)
    context = {
        'data': res
    }
    return render(request, 'transaction_details.html', context)
