from django.urls import path
from . import views

app_name = "fecoval"
urlpatterns = [
    # path("avaluos/", views.AvaluoList.as_view(), name="list"),
    path("create/", views.avaluos_create, name="create"),
]
