import requests
from bs4 import BeautifulSoup

#######################################
""" def analyzeHtml(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup """
#######################################
""" url = 'http://terraria.arcenserv.info/wiki/%E3%82%A2%E3%82%A4%E3%83%86%E3%83%A0'
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
print(category_data_list)

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
print(kinnsetu_childCategory_data_list) """

############################################################################
#武器の短剣情報をスクレイピングしてみよう(銅の短剣、金の短剣)。     
#各URLをリクエストするために短剣の名前のリストを作る。
res = requests.get('http://terraria.arcenserv.info/wiki/%E6%AD%A6%E5%99%A8')
soup = BeautifulSoup(res.text, 'html.parser')

tanken_names_for_search_table = soup.find_all('table', limit=2)

tanken_table = tanken_names_for_search_table[1]#短剣のテーブルだけ抽出
tanken_table_tr_list = tanken_table.find_all('tr')#テーブルの行の要素をリストで返す。

tanken_names_list_for_search = []
for i in range(1, len(tanken_table_tr_list)):
    tanken_want_name_elem = tanken_table_tr_list[i].find_all('td')[1] #ここに欲しい名前が入ってる！
    tanken_want_name_text = tanken_want_name_elem.text[:-1]
    tanken_names_list_for_search.append(tanken_want_name_text)
#print(tanken_names_list_for_search)

#tanken_names_list_for_searchに短剣で使う名前が入ってる。
##ここからは各ページからname,image_url,workplace,material,howtogetを取得する。
res_list = []
for tanken_name_for_url in tanken_names_list_for_search:
    res = requests.get(f'http://terraria.arcenserv.info/wiki/{tanken_name_for_url}')
    res_list.append(res)
tanken_names_list = []
tanken_image_urls_list = []
tanken_item_workplaces_list = []
tanken_item_materials_list = []
#ここのfor文ないに入れればURLごとにチェックできるよ。
for i in range(0, len(res_list)):
    soup = BeautifulSoup(res_list[i].text, 'html.parser')
    tanken_item_table = soup.find('table')
    th_tag = tanken_item_table.find('th')
    image_tag = tanken_item_table.find('img')

    #####
    # workplace,materialのテーブルから情報収集。
    try:
        workplace_and_material_table = soup.find_all('table', limit=2)[1]#多分gradiusの短剣でリスト超えエラーが出てる。 
        workplace_and_material_table_tr = workplace_and_material_table.find_all('tr', limit=2)[0]
        workplace_and_material_table_tr_a = workplace_and_material_table_tr.find_all('a')
    except IndexError as indexError:
        pass
        tanken_names_list.append(th_tag.text[:-1])
        tanken_image_urls_list.append(image_tag['src'])
        tanken_item_workplaces_list.append(['ーーーーー'])
        tanken_item_materials_list.append(['ーーーーー'])
        break #ここで強制終了されてるからGradiusが入ってないかと。

    try:
        workplace_and_material_table = soup.find_all('table', limit=2)[1]
        material_table_tr_elem = workplace_and_material_table.find_all('tr', limit=2)[1]
        material_table_tr_a_elems = material_table_tr_elem.find_all('a') #必要素材の行にあるaタグを全部取得してリストで返してる。
    except IndexError as indexError:
        #print(indexError)
        #tanken_item_materials_list.append(['ーーーーー']) #次回はここから修正する
        break

    #####
    # nameリストとimage_urlに格納していく。
    th_tag_name = th_tag.text[:-1]#stripで末尾だけ除外した。
    print(th_tag_name)
    tanken_names_list.append(th_tag_name) 
    tanken_image_urls_list.append(image_tag['src'])
    #####

    #######
    # workplaceはこっから記述してね。
    tanken_workplace_list_kuuhaku = []
    for workplace_elem in workplace_and_material_table_tr_a:
        tanken_workplace_list_kuuhaku.append(workplace_elem.text)
    #空白がないリストを生成する(奇数番目だけピックアップする)。
    tanken_workplace_name_list = []
    for i in range(0, len(tanken_workplace_list_kuuhaku)):
        if i%2 != 0:
            tanken_workplace_name_list.append(tanken_workplace_list_kuuhaku[i]) #奇数番だけアペンド。これで欲しい名前のリストが入ってる。
    tanken_item_workplaces_list.append(tanken_workplace_name_list) #リストの中にリストが入ってる状態。
    ######

    #######
    # item_materialはこっから記述してね。
    tanken_material_name_list_kuuhaku = []
    for material_table_tr_a_elem in material_table_tr_a_elems:
        tanken_material_name_list_kuuhaku.append(material_table_tr_a_elem.text)
    #空白がないリストを生成する。
    tanken_material_name_list = []
    for i in range(0, len(tanken_material_name_list_kuuhaku)):
        if i%2 != 0:
            tanken_material_name_list.append(tanken_material_name_list_kuuhaku[i])
    tanken_item_materials_list.append(tanken_material_name_list)
print(tanken_names_list)
print(tanken_image_urls_list)
print(tanken_item_workplaces_list)
print(tanken_item_materials_list)
############################################################################

###見本
""" tanken_workplace_list = ['銅の金床', '銀の金床']
tanken_needed_material_list = ['銅×7', '銀×7']
tanken_how_to_get = ['クラフティング', 'クラフティング'] """
####

###見本
""" tanken_workplace_list = ['銅の金床', '銀の金床']
tanken_needed_material_list = ['銅×7', '銀×7']
tanken_how_to_get = ['クラフティング', 'クラフティング'] """
#↓対応表(例)
""" tanken_workplace_list = ['56', '57']
tanken_needed_material_list = ['12', '13']
tanken_how_to_get = ['クラフティング', '敵を倒して12％の確率でドロップ'] """
####

###スクレイピングで用意する（for文で回す前に）
""" res = requests.get('http://terraria.arcenserv.info/wiki/Copper_Shortsword')
soup = BeautifulSoup(res.text, 'html.parser')
workplace_material_table = soup.find_all('table', limit=2)[1] 
###まずは必要家具からリストに格納
workplace_material__table_tr = workplace_material_table.find_all('tr', limit=2)[0]
workplace_material__table_tr_a = workplace_material__table_tr.find_all('a')

tanken_workplace_list_kuuhaku = []
for workplace_elem in workplace_material__table_tr_a:
    tanken_workplace_list_kuuhaku.append(workplace_elem.text)

#print(tanken_workplace_list_kuuhaku)
#空白がないリストを生成する。
tanken_workplace_name_list = []
for i in range(0, len(tanken_workplace_list_kuuhaku)):
    if i%2 != 0:
        tanken_workplace_name_list.append(tanken_workplace_list_kuuhaku[i]) #奇数番だけアペンド
print(tanken_workplace_name_list) """

###次に、必要素材を銅の短剣のページで取得してみる。
""" res = requests.get('http://terraria.arcenserv.info/wiki/Copper_Shortsword')
soup = BeautifulSoup(res.text, 'html.parser')
workplace_and_material_table = soup.find_all('table', limit=2)[1]
material_table_tr_elem = workplace_and_material_table.find_all('tr', limit=2)[1]
material_table_tr_a_elems = material_table_tr_elem.find_all('a') #必要素材の行にあるaタグを全部取得してリストで返してる。

tanken_material_name_list_kuuhaku = []
for material_table_tr_a_elem in material_table_tr_a_elems:
    tanken_material_name_list_kuuhaku.append(material_table_tr_a_elem.text)
#空白がないリストを生成する。
tanken_material_name_list = []
for i in range(0, len(tanken_material_name_list_kuuhaku)):
    if i%2 != 0:
        tanken_material_name_list.append(tanken_material_name_list_kuuhaku[i])
#print(tanken_material_name_list) """

tanken_how_to_get = ['クラフティング', 'クラフティング', 'クラフティング', 'クラフティング', 'クラフティング'
, 'クラフティング', 'クラフティング', 'クラフティング', 'クラフティング']
#用意した連想配列にnameとimage_urlを代入していく。
items_data_list = {}
items_data_list['name'] = tanken_names_list
items_data_list['image_url'] = tanken_image_urls_list
items_data_list['item_workplace'] = tanken_item_workplaces_list
items_data_list['item_needed_material'] = tanken_item_materials_list
items_data_list['how_to_get'] = tanken_how_to_get
#print(items_data_list) 
