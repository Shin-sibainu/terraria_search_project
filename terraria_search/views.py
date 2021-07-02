from django.shortcuts import render
from .models import ParentCategory, Category, Items
#from .scriping import parentCategories

def homeView(request):
  domain_url = request.META.get("HTTP_HOST")
  ########
  # ここで親カテゴリーデータを一括作成してみる。 
  #for i in range(len(parentCategories['name'])):
  #  ParentCategory.objects.create(name=parentCategories['name'][i], image_url=parentCategories['image_url'][i])
  # 一度だけ呼べばいい。データ格納だけだから。
  ########
  paretnCategory_data = ParentCategory.objects.all()

  context = {
    'domain_url': domain_url,
    'parentCategory_data': paretnCategory_data
  }
  return render(request, 'home.html', context)


def categoryView(request, category_name):
  domain_url = request.META.get("HTTP_HOST")

  context = {
    
  }
  return render(request, 'category.html', context)
