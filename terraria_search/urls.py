from terraria_search_project.settings import STATIC_ROOT, STATIC_URL
from django.urls import path
from django.urls.conf import include
from .views import homeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', homeView, name='home')
] + static(settings.STATIC_URL, document_root=STATIC_ROOT)