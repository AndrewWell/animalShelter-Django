from django.contrib import admin

# Register your models here.
from .models import Dogs
from .models import Cats
from .models import Carousel

admin.site.register(Dogs)
admin.site.register(Cats)
admin.site.register(Carousel)
