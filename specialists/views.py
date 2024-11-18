from rest_framework import viewsets
from .models import Specialist
from .serializers import SpecialistSerializer


class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
