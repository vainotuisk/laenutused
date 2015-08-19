from django.contrib import admin

# Register your models here.
from .models import Kohad, Liik, Asi, Kes, Laenutused
# Register your models here.
admin.site.register(Kohad)
admin.site.register(Liik)
admin.site.register(Asi)
admin.site.register(Kes)
admin.site.register(Laenutused)
