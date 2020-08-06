from django.urls import path

from . import views

app_name = "carsapp"

urlpatterns = [
    path("", views.CarListView.as_view(), name="list_by_cars"),
]
