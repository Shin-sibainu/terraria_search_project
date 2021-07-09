from django.shortcuts import render
from .models import ChildCategory, ParentCategory, Category, Items
#from .scriping import parentCategories
#from .scriping import category_data_list
#from .scriping import kinnsetu_childCategory_data_list
from .scriping import items_data_list

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


"""   ###アイテムデータの格納。childCategoryによって入れるデータが違う。銅の短剣だけなら特定の値を入れれば良かった。
  ###一応nameとimage_urlは連想配列かとってこれてる。あとはitem_workplaceとitem_needed_materialをどうやってaddするかが問題。
  parentCategoryObj = ParentCategory.objects.get(name='武器')
  categoryObj = Category.objects.get(name='近接武器')
  childcategoryObj = ChildCategory.objects.get(name='短剣')
  #必要な素材は鉄の金床とすずの金床とか武器によって違うからここはfor文だよな。
  item_workplaceObj= Items.objects.get(name='鉄の金床')
  item_needed_materialObj= Items.objects.get(name='鉄の金床')

  for i in range(len(items_data_list['name'])): 
    instance = Items.objects.create(
      name=items_data_list['name'][i],
      image_url=items_data_list['image_url'][i],
      parentCategory_id=parentCategoryObj,
      how_to_get=items_data_list['how_to_get'][i]
    )
    #ManyToManyはaddでしか入れられない。
    instance.category.add(categoryObj)#id=7番が近接武器。
    instance.childcategory.add(childcategoryObj)#id=23番が短剣。
  ###item_workplacetとitem_needed_materialを登録する。1つには番号指定できない。
    instance.item_workplace.add(item_workplaceObj)#金床とか登録してないから番号していできない・・・。
    instance.item_needed_material.add(item_needed_materialObj)#素材の番号とかえげつない量になるぞこれ・・・。
    #もしかしてaddだったら元々ItemsにデータがないとダメだからUpdateで更新すればいいのかな？　 """