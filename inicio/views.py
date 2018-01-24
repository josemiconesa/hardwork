from django.shortcuts import render

# Create your views here.

def inicio(request):
    context = {
        "author": "José Miguel",
    }
    return render(request, "inicio.html", context)

def productos(request):
    return render(request, "productos.html", {})

def faq(request):
    return render(request, "faq.html", {})

def about(request):
    return render(request, "about.html", {})

def contacto(request):
    return render(request, "contacto.html", {})

#http://img.wallpaperfolder.com/f/4A3157A55FC9/work-hard-dream-big-ipad.jpg
