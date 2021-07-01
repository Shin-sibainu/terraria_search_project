import requests
from bs4 import BeautifulSoup

url = 'http://terraria.arcenserv.info/wiki/%E3%82%A2%E3%82%A4%E3%83%86%E3%83%A0'
r = requests.get(url) #Responseオブジェクトを返す。

soup = BeautifulSoup(r.text, 'html.parser')
parent_category_table = soup.find('table')#カテゴリーに関連するテーブル

#親カテゴリーの各名前をスクレイピング
parent_category_names = parent_category_table.find_all('a')
parent_category_names_list = []
for parent_category_name in parent_category_names:
    parent_category_names_list.append(parent_category_name.text)
parent_category_names_list.pop(len(parent_category_names_list)-1)
#print(parent_category_names_list)

#親カテゴリーの各カテゴリーのURLをスクレイピング
parent_category_image_urls = parent_category_table.find_all('img')
parent_category_image_urls_list = []
for parent_category_image_url in parent_category_image_urls:
    parent_category_image_urls_list.append(parent_category_image_url['src'])
#print(parent_category_image_urls_list)

#親カテゴリーのデータが入ったら連想配列を用意
parentCategories = {}

#nameキーに値として名前のリストを格納する。
parentCategories['name'] = parent_category_names_list
parentCategories['image_url'] = parent_category_image_urls_list

print(parentCategories['name'])

for i in enumerate(parentCategories['name']):
    print(i[0])
    #parentCategories['name'][i]