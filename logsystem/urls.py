from django.urls import path
from logsystem import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("Coils/", views.Coils, name="coils"),
    path("Coils/Detail/", views.Coil_Detail, name="coil_detail"),
]