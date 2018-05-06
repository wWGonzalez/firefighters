from rest_framework import serializers

from users.models import Persona

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Persona
		fields = ('dpi','coordenadas','direccion', 'emergencia')
