import django_filters
from carsapp.models import Car

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = [ 'manufacturer', 'model', 'year', 'color', ]