from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnico, Cliente
from django.http import HttpResponse, HttpResponseRedirect
from .form import TecnicoForm, ClienteForm, OrdenForm
from django.core import serializers

# Create your views here.


def index(request):
    index = 'index.html'
    return render(request, index)


def login(request):
    login = 'login.html'
    return render(request, login)


def iniciarsesion(request):
    usuario = request.POST.get('username')
    password = request.POST.get('password')
    objeto = Tecnico.objects.get(usuario=usuario, password=password)
    print(objeto)
    if(objeto.es_administrador == True):
        return HttpResponseRedirect('/administracion/')
    if(objeto.es_tecnico == True):
        cli = Cliente.objects.filter(tecnicoAsignado=objeto)
        pagina = 'clientes.html'
        contexto = {'cli': cli}
        return render(request, pagina, contexto)
    else:
        return HttpResponseRedirect('/404/')


def administracion(request):
    tec = Tecnico.objects.all()
    cli = Cliente.objects.all()
    return render(request, 'administracion.html', {'tec': tec, 'cli': cli})

# -------------------------------------------------------------


def administracion_eliminar(request, pk):
    Tecnico.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/administracion/')


def administracion_editar(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    if request.method == "POST":
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            tecnico = form.save(commit=False)
            tecnico.save()
            return HttpResponseRedirect('/administracion/')
    else:
        form = TecnicoForm(instance=tecnico)
        return render(request, 'editar_tecnico.html', {'form': form})


def administracion_nuevo(request):
    if request.method == "POST":
        form = TecnicoForm(request.POST)
        if form.is_valid():
            tecnico = form.save(commit=False)
            tecnico.save()
            return HttpResponseRedirect('/administracion/')
    else:
        form = TecnicoForm()
        return render(request, 'editar_tecnico.html', {'form': form})

# -----------------------------------------------------


def cliente_eliminar(request, pk):
    Cliente.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/administracion/')


def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return HttpResponseRedirect('/administracion/')
    else:
        form = ClienteForm(instance=cliente)
        return render(request, 'editar_cliente.html', {'form': form})


def cliente_nuevo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return HttpResponseRedirect('/administracion/')
    else:
        form = ClienteForm()
        return render(request, 'editar_cliente.html', {'form': form})

# ----------------------------------------------------


def clientes(request):
    cli = Cliente.objects.all()
    clientes = 'clientes.html'
    return render(request, clientes, {'cli': cli})

# --------------------------------------------------------

def orden(request, pk):
    if request.method == "POST":
        tecnico = get_object_or_404(Tecnico, pk=pk)
        print(pk)
        form = OrdenForm(request.POST, initial={"tecnico": tecnico})
        if form.is_valid():
            orden = form.save(commit=False)
            orden.save()
            return HttpResponseRedirect('/login/')
    else:
        form = OrdenForm()
        return render(request, 'editar_orden.html', {'form': form})

# ----------------------------------------------------------------------


def getdata(request):
    results = Tecnico.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)
