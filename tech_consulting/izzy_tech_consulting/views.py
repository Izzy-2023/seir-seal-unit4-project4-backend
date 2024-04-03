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

class CustomView(APIView):
    def get(self, request):
        # Your custom logic here
        return Response({"message": "Hello, this is a custom view!"})

class ServiceListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BookAppointment(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=404)

        data = {
            "service": service.id,
            "customer": None,  # Assuming you'll handle this in the frontend
            "appointment_date": request.data.get("date"),
            "status": "pending",  # Assuming the status is always pending initially
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "email": request.data.get("email"),
        }

        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

