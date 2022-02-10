from django.shortcuts import render

# Create your views here.
from productos.models import Producto


def listar(request):
   print(request.method)
   list = Producto.objects.all()
   return render(request, 'productos/index.html', {"list": list})
