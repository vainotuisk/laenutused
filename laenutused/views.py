from django.views import generic
from django.views.generic.list import ListView
from laeutusteapp.models import Laenutused

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class LaenutusedPage(generic.TemplateView):
    template_name = "laenutused.html"
# class laenutusedListView(ListView):
#     model = kuup
