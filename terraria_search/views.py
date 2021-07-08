from django.shortcuts import render
from .models import ChildCategory, ParentCategory, Category, Items
#from .scriping import parentCategories
#from .scriping import category_data_list
#from .scriping import kinnsetu_childCategory_data_list
#from .scriping import items_data_list

def homeView(request):
  domain_url = request.META.get("HTTP_HOST")
  ########
  # ここで親カテゴリーデータを一括作成してみる。 
  #for i in range(len(parentCategories['name'])):
  #  ParentCategory.objects.create(name=parentCategories['name'][i], image_url=parentCategories['image_url'][i])
  # 一度だけ呼べばいい。データ格納だけだから。
  ########
  parentCategory_data = ParentCategory.objects.all()

  context = {
    'domain_url': domain_url,
    'parentCategory_data': parentCategory_data
  }
  return render(request, 'home.html', context)


def categoryView(request, parentCategory_name):
  domain_url = request.META.get("HTTP_HOST")

  #parentCategoryObj = ParentCategory.objects.get(name='武器')
  #for i in range(len(category_data_list['name'])):
  #  Category.objects.create(name=category_data_list['name'][i], image_url=category_data_list['image_url'][i], parentCategory_id=parentCategoryObj)
  category_data = Category.objects.all()

  context = {
    'domain_url': domain_url,
    'category_data': category_data
  }
  return render(request, 'category.html', context)


def childCategoryView(request, category_name):
  domain_url = request.META.get("HTTP_HOST")

  #parentCategoryObj = ParentCategory.objects.get(name='武器')
  #for i in range(len(category_data_list['name'])):
  #  Category.objects.create(name=category_data_list['name'][i], image_url=category_data_list['image_url'][i], parentCategory_id=parentCategoryObj)


  #categoryObj = Category.objects.get(name='近接武器')
  #for i in range(len(kinnsetu_childCategory_data_list['name'])):
  #  ChildCategory.objects.create(name=kinnsetu_childCategory_data_list['name'][i], image_url=kinnsetu_childCategory_data_list['image_url'][i], category_id=categoryObj)
  #childCategory_data = Category.objects.all()
  childCategory_data = ChildCategory.objects.all()

  context = {
    'domain_url': domain_url,
    'childCategory_data': childCategory_data
  }
  return render(request, 'childCategory.html', context) 


def childCategoryItemsView(request, childCategory_name):
  ###アイテムデータの格納。childCategoryによって入れるデータが違う。銅の短剣だけなら特定の値を入れれば良かった。
  ###一応nameとimage_urlは連想配列かとってこれてる。あとはitem_workplaceとitem_needed_materialをどうやってaddするかが問題。
  ###
  #parentCategoryObj = ParentCategory.objects.get(name='武器')
  #ManytoManyFieldはモデルのインスタンスにaddしないといけないらしい。
  #categoryObj = Category.objects.get(name='近接武器')
  #childCategoryObj = ChildCategory.objects.get(name='短剣')
  #ここに登録するときitem_workplaceとitem_needed_materialを登録すること。
  #必要な家具とか素材は1つ1つバラバラだからどうしよう。

  #for i in range(len(items_data_list['name'])): 
  #  instance = Items.objects.create(
  #  name=items_data_list['name'][i],
  #  image_url=items_data_list['image_url'][i],
  #  parentCategory_id=parentCategoryObj,
  #　how_to_get=items_data_list['how_to_get'][i],
  #  )
  #  instance.category.add(7)#id=7番が近接武器。
  #  instance.childcategory.add(23)#id=23番が短剣。
  ###item_workplacetとitem_needed_materialを登録する。1つには番号指定できない。
  #  instance.item_workplace.add(items_data_list['item_workplace'][i])? これは番号を指定することになりそう。
  #  instance.item_needed_material.add(items_data_list['item_needed_material'][i])?
  #Itemsデータを全取得
  item_data = Items.objects.all()

  context = {
    'item_data': item_data  
  }
  return render(request, 'childCategoryItem.html', context)

def ItemView(request, item_name):
  item_data = Items.objects.get(name=item_name)
  context = {
    'item_data': item_data
  }
  return render(request, 'item.html', context)
