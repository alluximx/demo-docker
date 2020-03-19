from django.urls import path
from . import views

app_name = "fecoval"
urlpatterns = [
    path("", views.AvaluoList.as_view(), name="list"),
    path("create/", views.AvaluoCreate.as_view(), name="create"),
]
