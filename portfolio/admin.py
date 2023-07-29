from django.contrib import admin

# Register your models here.
from .models import Cadeira
from .models import Portfolio

admin.site.register(Portfolio)
admin.site.register(Cadeira)

