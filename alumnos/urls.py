from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AlumnoViewSet,
    CursoViewSet,
    InscripcionViewSet,
    buscar_alumno_ci,
    alumnos_por_curso
)

router = DefaultRouter()

router.register("alumnos", AlumnoViewSet)
router.register("cursos", CursoViewSet)
router.register("inscripciones", InscripcionViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path(
        "buscar-alumno/<str:ci>/",
        buscar_alumno_ci
    ),

    path(
        "curso/<int:curso_id>/alumnos/",
        alumnos_por_curso
    ),
]