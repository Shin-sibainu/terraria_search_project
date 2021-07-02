from terraria_search_project.settings import STATICFILES_DIRS, STATIC_URL
from django.urls import path
from .views import homeView, categoryView, childCategoryView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', homeView, name='home'),
  path('parentCategory/<str:parentCategory_name>/', categoryView, name='parentCategory'),
  path('category/<str:category_name>', childCategoryView, name='category')
] + static(settings.STATIC_URL, document_root=STATICFILES_DIRS) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)