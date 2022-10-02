from multiprocessing import context
from django.http import HttpResponse
from datetime import date, datetime
from django.template import Context, Template, loader
import random

from familiares.models import Familiar

def crearFamiliares(request):
    # crear 3 familiares
    familiar1 = Familiar(nombre = 'Pablo', apellido = 'Leonczik', edad = random.randrange(1,100), fechaCreacion = datetime.now())
    familiar2 = Familiar(nombre = 'Pepe', apellido = 'Leoncio', edad = random.randrange(1,100), fechaCreacion = datetime.now())
    familiar3 = Familiar(nombre = 'Pepa', apellido = 'Leoncito', edad = random.randrange(1,100), fechaCreacion = datetime.now())
    
    # registrar familar a la base de datos
    familiar1.save()
    familiar2.save()
    familiar3.save()

    template = loader.get_template("crearFamiliares.html")
    templateRenderizado = template.render({})
    return HttpResponse(templateRenderizado)

def verFamiliares(request):

    familiares = Familiar.objects.all()
    
    template = loader.get_template("verFamiliares.html")
    templateRenderizado = template.render({'familiares': familiares})

    return HttpResponse(templateRenderizado)