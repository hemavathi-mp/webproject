from django.urls import include, path
from .views import *

urlpatterns = [
    path('machine/', MachineViewSet.as_view()),
    path('machine/<pk>/', MachineViewSet.as_view()),
    path('axis/', AxisViewSet.as_view()),
    path('axis/<pk>/', AxisViewSet.as_view()),
    path('axisvalue/', AxisValueViewSet.as_view()),
    path('axisvalue/<pk>/', AxisValueViewSet.as_view()),

]
