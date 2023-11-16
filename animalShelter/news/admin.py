from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Articles
from .models import PrepositionalNews


admin.site.register(Articles)
admin.site.register(PrepositionalNews)

