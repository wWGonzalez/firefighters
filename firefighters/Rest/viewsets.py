from rest_framework import generics
from rest_framework import viewsets

from .serializers import PersonaSerializer
from users.models import Persona

class AlertViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer
