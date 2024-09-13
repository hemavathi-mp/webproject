# serializers.py
from rest_framework import serializers
from machine.models import Machine, Axis, AxisValue

class AxisValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxisValue
        fields = '__all__'

class AxisSerializer(serializers.ModelSerializer):
    values = AxisValueSerializer(many=True, read_only=True)

    class Meta:
        model = Axis
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    axes = AxisSerializer(many=True, read_only=True)

    class Meta:
        model = Machine
        fields = '__all__'
