from django.shortcuts import render
from .models import ParentCategory, Category, Items
#from .scriping import parentCategories
from .scriping import category_data_list

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


def categoryView(request, parentCategory_name):
  domain_url = request.META.get("HTTP_HOST")

  #parentCategoryObj = ParentCategory.objects.get(name='武器')
  #for i in range(len(category_data_list['name'])):
  #  Category.objects.create(name=category_data_list['name'][i], image_url=category_data_list['image_url'][i], parentCategory_id=parentCategoryObj)
  category_data = Category.objects.all()

  context = {
    'category_data': category_data
  }
  return render(request, 'category.html', context)


def childCategoryView(request, category_name):
  return render(request, 'childCategory.html', {})
