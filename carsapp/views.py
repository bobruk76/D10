from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import redirect, render

from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from carsapp.models import Car
from carsapp.forms import CarForm
from carsapp.filters import CarFilter


class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class CarListView(FormListView):
    template_name = "list.html"
    form_class = CarForm
    paginate = 50

    def get_queryset(self):
        return Car.objects.all()

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


def car_list(request):
    template = loader.get_template('list_filter.html')
    f = CarFilter(request.GET, queryset=Car.objects.all())
    contex = {
        'filter': f,
    }
    return HttpResponse(template.render(contex, request))

# def book_increment(request):
#     if request.method == 'POST':
#         book_id = request.POST['id']
#         if not book_id:
#             return redirect('/books/')
#         else:
#             book = Book.objects.filter(id=book_id).first()
#             if not book:
#                 return redirect('/books/')
#             book.copy_count += 1
#             book.save()
#         return redirect('/books/')
#     else:
#         return redirect('/books/')