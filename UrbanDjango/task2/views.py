from django.shortcuts import render
from django.views.generic import TemplateView


def index_for_func(request):
    return render(request, 'second_task/for_func.html')


class IndexForClass(TemplateView):
    template_name = 'second_task/for_class.html'
