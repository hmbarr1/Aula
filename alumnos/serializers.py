from rest_framework import serializers
from .models import Alumno,Curso, Inscripcion

class AlumnoSerializer(serializers.ModelSerializer):
	class Meta:
		model= Alumno
		fields= '__all__'
class CursoSerializer(serializers.ModelSerializer):
	class Meta:
		model= Curso
		fields= '__all__'
class InscripcionSerializer(serializers.ModelSerializer):
	class Meta:
		model= Inscripcion
		fields='__all__'
