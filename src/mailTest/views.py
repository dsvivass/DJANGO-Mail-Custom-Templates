from django.shortcuts import render
import os

# Create your views here.
def homeView(request, *args, **kwargs): # Cada función llega con un request definido
    # Este request.user es fundamental, así vemos quién solicita esto
    # return HttpResponse("<h1>Hello World!</h1>") # Esto sirve, pero ahora vamos a manejar templates
    print(os.getcwd())
    return render(request, "home.html", {})
