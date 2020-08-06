from django.db import models

# Create your models here.
# Необходимо описать модель автомобиля (Car) с полями:
# производитель (BMW, Audi, Tesla и т.д.) (CharField)
# модель авто (S, TT, X6 и т.д.) (CharField)
# год выпуска (IntegerField)
# коробка передач (SmallIntegerField with choices "механика", "автомат", "робот")
# цвет
class Manufacturer(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'

    def __str__(self):
        return f'{self.name}'

class Car(models.Model):
    TRANSMISSION_MANUAL = 1
    TRANSMISSION_AUTOMAT = 2
    TRANSMISSION_ROBOT = 3

    TRANSMISSION_CHOICES = [
        (TRANSMISSION_MANUAL, "Механическая"),
        (TRANSMISSION_AUTOMAT, "Автомат"),
        (TRANSMISSION_ROBOT, "Робот"),
    ]


    model = models.CharField(max_length=256, verbose_name='Модель')
    slug = models.SlugField
    manufacturer = models.ForeignKey(Manufacturer, default=None, on_delete=models.DO_NOTHING , verbose_name='Производитель')
    transmission = models.IntegerField(
        "Коробка", choices=TRANSMISSION_CHOICES, default=TRANSMISSION_AUTOMAT
    )
    color = models.CharField(max_length=256, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобиль'

    def __str__(self):
        return '{} -- {}'.format(self.model, self.color)