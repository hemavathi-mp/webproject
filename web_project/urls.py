"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from machine.views import MachineViewSet, AxisViewSet, AxisValueViewSet

from django.urls import re_path
from machine.consumers import MachineDataConsumer


router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'axes', AxisViewSet)
router.register(r'axis-values', AxisValueViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

websocket_urlpatterns = [
    re_path(r'ws/machine-data/$', MachineDataConsumer.as_asgi()),
]