from django.shortcuts import render

# Create your views here.
# views.py
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from user.serializers import RegisterUserSerializer
from machine.models import Machine, Axis, AxisValue
from machine.serializers import MachineSerializer, AxisSerializer, AxisValueSerializer
from user.permission import IsManagerOrSuperAdmin


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
