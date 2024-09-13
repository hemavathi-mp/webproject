from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

class Axis(models.Model):
    name = models.CharField(max_length=10)  # X, Y, Z, A, C
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='axes')

class AxisValue(models.Model):
    axis = models.ForeignKey(Axis, on_delete=models.CASCADE, related_name='values')
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['axis', 'timestamp']),
        ]
