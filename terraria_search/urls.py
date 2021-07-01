from terraria_search_project.settings import STATICFILES_DIRS, STATIC_URL
from django.urls import path
from django.urls.conf import include
from .views import homeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', homeView, name='home')
] + static(settings.STATIC_URL, document_root=STATICFILES_DIRS) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)