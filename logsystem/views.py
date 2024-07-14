from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "home.html")

def Coils(request):
    return render(request, "coils.html")

def Coil_Detail(request):
    return render(request, "coil_detail.html")