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




def control_page(request):

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "urine":
            ValveControl.objects.all().delete()
            ValveControl.objects.create(state=True)

        elif action == "noturine":
            ValveControl.objects.all().delete()
            ValveControl.objects.create(state=False)

    status = ValveControl.objects.first()

    return render(request, "control.html", {"status": status})


@api_view(['GET'])
def get_valve_state(request):

    state = ValveControl.objects.first()

    if state:
        return Response({"state": state.state})

    return Response({"state": False})