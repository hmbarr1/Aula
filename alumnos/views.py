from rest_framework.viewsets import ModelViewSet
from .models import Alumno, Curso, Inscripcion
from .serializers import(AlumnoSerializer, CursoSerializer, InscripcionSerializer)
from rest_framework.decorators import api_view
from rest_framework.response import Response


class AlumnoViewSet(ModelViewSet):
	queryset= Alumno.objects.all()
	serializer_class= AlumnoSerializer

class CursoViewSet(ModelViewSet):
	queryset= Curso.objects.all()
	serializer_class= CursoSerializer
class InscripcionViewSet(ModelViewSet):
	queryset= Inscripcion.objects.all()
	serializer_class= InscripcionSerializer

@api_view(['GET'])
def buscar_alumno_ci(request, ci):

    alumno = Alumno.objects.get(ci=ci)

    cursos = []

    for inscripcion in Inscripcion.objects.filter(alumno=alumno):
        cursos.append(inscripcion.curso.nombre)

    return Response({
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "ci": alumno.ci,
        "cursos": cursos
    })

@api_view(['GET'])
def alumnos_por_curso(request, curso_id):

    curso = Curso.objects.get(id=curso_id)

    alumnos = []

    for inscripcion in Inscripcion.objects.filter(curso=curso):
        alumnos.append({
            "nombre": inscripcion.alumno.nombre,
            "apellido": inscripcion.alumno.apellido,
            "ci": inscripcion.alumno.ci
        })

    return Response({
        "curso": curso.nombre,
        "cantidad_alumnos": len(alumnos),
        "alumnos": alumnos
    })

