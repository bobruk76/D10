from django.shortcuts import render
from django.views.generic.list import ListView
from carsapp.models import Car
# Create your views here.

class CarListView(ListView):
    model = Car
    paginate_by = 100
    template_name = "list.html"

    # def get_queryset(self):
    #     u = self.request.user
    #     qs = super().get_queryset()
    #     return qs.filter(owner=u)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     user_tasks = self.get_queryset()
    #     tags = []
    #     for t in user_tasks:
    #         tags.append(list(t.category.all()))

    #     categories = []
    #     for cat in t.category.all():
    #         if cat not in categories:
    #             categories.append(cat)
    #     context["categories"] = categories

    #     return context