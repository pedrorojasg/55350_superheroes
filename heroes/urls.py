from django.urls import path

from heroes.views import listar_heroes, eliminar_heroe, crear_heroe, editar_heroe

# Son las URLS especificas de la app
urlpatterns = [
    path("heroes/", listar_heroes, name="listar_heroes"),
    path("crear-heroe/", crear_heroe, name="crear_heroe"),
    path("editar-heroe/<int:id>/", editar_heroe, name="editar_heroe"),
    path("eliminar-heroe/<int:id>/", eliminar_heroe, name="eliminar_heroe"),
]
