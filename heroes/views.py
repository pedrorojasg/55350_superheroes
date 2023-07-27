from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from heroes.models import Heroe, Villano
from heroes.forms import HeroeFormulario

# Create your views here.

def listar_heroes(request):
    contexto = {
        "heroes": Heroe.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='heroes/lista_heroes.html',
        context=contexto,
    )
    return http_response


def eliminar_heroe(request, id):
    heroe = Heroe.objects.get(id=id)
    if request.method == "POST":
        # borra el heroe de la base de datos
        heroe.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('listar_heroes')
        return redirect(url_exitosa)


def crear_heroe(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = HeroeFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            nombre_real = data["nombre_real"]
            residencia = data["residencia"]
            # creo un heroe en memoria RAM
            heroe = Heroe(nombre=nombre, nombre_real=nombre_real, residencia=residencia)
            # Lo guardan en la Base de datos
            heroe.save()

            # Redirecciono al usuario a la lista
            url_exitosa = reverse('listar_heroes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = HeroeFormulario()
    http_response = render(
        request=request,
        template_name='heroes/formulario_heroe.html',
        context={'formulario': formulario}
    )
    return http_response


def editar_heroe(request, id):
    heroe = Heroe.objects.get(id=id)
    if request.method == "POST":
        formulario = HeroeFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            heroe.nombre = data['nombre']
            heroe.nombre_real = data['nombre_real']
            heroe.residencia = data['residencia']
            heroe.save()

            url_exitosa = reverse('listar_heroes')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': heroe.nombre,
            'nombre_real': heroe.nombre_real,
            'residencia': heroe.residencia,
        }
        formulario = HeroeFormulario(initial=inicial)
    return render(
        request=request,
        template_name='heroes/formulario_heroe.html',
        context={'formulario': formulario},
    )
