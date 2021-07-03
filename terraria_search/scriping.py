import requests
from bs4 import BeautifulSoup

#######################################
def analyzeHtml(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
#######################################
""" url = 'http://terraria.arcenserv.info/wiki/%E3%82%A2%E3%82%A4%E3%83%86%E3%83%A0'
r = requests.get(url) #Responseオブジェクトを返す。

soup = BeautifulSoup(r.text, 'html.parser') """
""" parent_category_table = soup.find('table')#カテゴリーに関連するテーブル

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
parentCategories['image_url'] = parent_category_image_urls_list """

""" #################################
#武器のカテゴリーの名前と画像パスをスクレイピングしてみよう。
soup = analyzeHtml('http://terraria.arcenserv.info/wiki/%E6%AD%A6%E5%99%A8')

#名前をスクレイピング
category_name_table = soup.find_all('span', class_='toctext')
category_and_childCategory_names_list = []
for category_name in category_name_table:
    category_and_childCategory_names_list.append(category_name.text)
#文字列の最後が「器」だったら、それ以外の要素を削除する。
category_names_list = []
for category_name_str in category_and_childCategory_names_list:
    last_word = category_name_str[len(category_name_str)-1]
    if(last_word == '器'):
        category_names_list.append(category_name_str)
#print(category_names_list)

#画像パスをスクレイピング。
#今回は自分で好き勝手に手動でリスト作成することにする。
category_image_urls_list = ['http://media.arcenserv.info/w/images/Platinum_Shortsword.png',
"http://media.arcenserv.info/w/images/Musket.png", 'http://media.arcenserv.info/w/images/Crystal_Storm.png',
"http://media.arcenserv.info/w/images/Stardust_Dragon_Staff.png", "http://media.arcenserv.info/w/images/Beenade.png",
"http://media.arcenserv.info/w/images/Holy_Water.png"]

#parentCategory_idの設定リストを作りたい。
#idに指定できるのはParentCategoryのModelオブジェクトだけみたいね。objects.get(neme="武器")で取得できた。

#連想配列作る。
category_data_list = {}
category_data_list['name'] = category_names_list
category_data_list['image_url'] = category_image_urls_list
print(category_data_list) """

#################################
#武器の子カテゴリーの名前をスクレイピングしてみよう(短剣、長剣、魔法剣、、)。
soup = analyzeHtml('http://terraria.arcenserv.info/wiki/%E6%AD%A6%E5%99%A8')
childCategory_names_li = soup.find('li')
childCategory_name_span = childCategory_names_li.find_all('span', class_='toctext')

kinnsetu_childCategory_names_list = []
for childCategory_name in childCategory_name_span:
    kinnsetu_childCategory_names_list.append(childCategory_name.text)
kinnsetu_childCategory_names_list.pop(0)
#print(kinnsetu_childCategory_names_list)

#画像パスをスクレイピング。
#今回は自分で好き勝手に手動でリスト作成することにする。
kinnsetu_childCategory_image_urls_list = ['http://media.arcenserv.info/w/images/Gold_Shortsword.png','http://media.arcenserv.info/w/images/Muramasa.png',
"http://media.arcenserv.info/w/images/Terra_Blade.png","http://media.arcenserv.info/w/images/Ghastly_Glaive.png",
"http://media.arcenserv.info/w/images/Flower_Pow.png","http://media.arcenserv.info/w/images/Solar_Eruption.png",
"http://media.arcenserv.info/w/images/Flamarang.png","http://media.arcenserv.info/w/images/Terrarian.png",
"http://media.arcenserv.info/w/images/Vampire_Knives.png"]

kinnsetu_childCategory_data_list = {}
kinnsetu_childCategory_data_list['name'] = kinnsetu_childCategory_names_list
kinnsetu_childCategory_data_list['image_url'] = kinnsetu_childCategory_image_urls_list
print(kinnsetu_childCategory_data_list)


        

