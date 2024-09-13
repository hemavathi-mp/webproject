from django.shortcuts import render

# Create your views here.
import pandas as pd
import numpy as np


from machine.models import Machine, Axis, AxisValue
from django.utils.timezone import now
from rest_framework import viewsets
from machine.models import Machine, Axis, AxisValue
from machine.serializers import MachineSerializer, AxisSerializer, AxisValueSerializer
from rest_framework.permissions import IsAuthenticated



# Generate values for X, Y, Z, A, C axes for 20 machines
def generate_values(interval, steps=100):
    return np.linspace(start=0, stop=interval * steps, num=steps)

def upload_file(request):
    # Load Excel file
    excel_file = request.data.get("file")

    df = pd.read_excel(excel_file)

    axes = ['X', 'Y', 'Z', 'A', 'C']
    machines = [f'Machine_{i+1}' for i in range(20)]

    data = {}
    for machine in machines:
        data[machine] = {axis: generate_values(df.loc[0, 'UPDATE INTERVAL']) for axis in axes}
    
    populate_db(data)


# Generated values will be stored in `data`

def populate_db(data):
    for machine_name, axes_data in data.items():
        machine, created = Machine.objects.get_or_create(name=machine_name)
        
        for axis_name, values in axes_data.items():
            axis, created = Axis.objects.get_or_create(name=axis_name, machine=machine)
            
            for value in values:
                AxisValue.objects.create(axis=axis, value=value, timestamp=now())




class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [IsAuthenticated]

class AxisViewSet(viewsets.ModelViewSet):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer
    permission_classes = [IsAuthenticated]

class AxisValueViewSet(viewsets.ModelViewSet):
    queryset = AxisValue.objects.all()
    serializer_class = AxisValueSerializer
    permission_classes = [IsAuthenticated]
