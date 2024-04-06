# views.py
from rest_framework import viewsets
from .models import Service, Appointment
from .serializers import ServiceSerializer, AppointmentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

class BookAppointment(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        service = Service.objects.filter(pk=pk).first()
        if not service:
            return Response({"error": "Service not found"}, status=404)
        
        appointment_data = request.data.copy()  # Create a mutable copy of the request data
        appointment_data['service'] = pk  # Explicitly add the service ID to the appointment data
        
        serializer = AppointmentSerializer(data=appointment_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
