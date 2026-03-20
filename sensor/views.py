from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from .models import UrineData, ValveControl






def home(request):
    return render(request,'home.html')


@api_view(['POST'])
def receive_data(request):

    volume = request.data.get('volume')

    UrineData.objects.create(volume=volume)

    return Response({"status": "saved"})




def dashboard(request):

    data = UrineData.objects.all().order_by('-created')

    return render(request,'dashboard.html',{'data':data})

import serial
import time
def control_page(request):

    state = "CLOSED"

    if request.method == "POST":

        action = request.POST.get("action")
        print("Button pressed:", action)

        try:
            ser = get_serial()

            if action == "urine":
                ser.write(b"URINE\n")
                state = "OPEN"

            elif action == "noturine":
                ser.write(b"NOT_URINE\n")
                state = "CLOSED"

        except Exception as e:
            print("Serial Error:", e)

    return render(request,"control.html",{"state":state})

@api_view(['GET'])
def get_valve_state(request):

    state = ValveControl.objects.first()

    if state:
        return Response({"state": state.state})

    return Response({"state": False})


ser = None

def get_serial():
    global ser
    if ser is None or not ser.is_open:
        ser = serial.Serial('COM3', 115200, timeout=1)
        time.sleep(2)  # wait for ESP reset
    return ser