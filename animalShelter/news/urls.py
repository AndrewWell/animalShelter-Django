from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.news_home, name='news_home'),
                  path('prepositionalNews', views.news_prepNews, name='prepNews')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
