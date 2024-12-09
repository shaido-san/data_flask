from flask import Flask
from flask import render_template

#インスタンス作成
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/item/value')
#def item(value):
 #   return render_template('item.html', value=value)

@app.route('/item')
def item():
    return render_template('item.html')

@app.route('/item/detail/<int:id>')
def item_detail(id):
    return render_template('detail.html', show_id=id)

# render_templateで複数の値を渡す
@app.route('/multiple')
def vshow_jinja_multiple():
    word1 = "わわわわわわわわあわわわわわわわわワワワワわわ"
    word2 = '忍者じゃないよ神社だよ'
    return render_template('jinja/show1.html', val1=word1, val2=word2)

# 辞書型

@app.route('/dict')
def show_jinja_dict():
    words = {
        'val1': "ンンンンンンンンンンンンんそそソソそ",
        'val2':"ジンジャー"
    }
    return render_template('jinja/show2.html', key=words)

# リスト型
@app.route('/list')
def show_jinja_list():
    word_list = ['ジンジャーーーーーー','ニンジャーーーーーーーー']
    return render_template('jinja/show3.html', words=word_list)

# クラス型
class users:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
         return f'名前：{self.name} 年齢：{self.age}'
    
@app.route('/class')
def show_jinja_class():
    user_list = users('徳川慶喜',123)
    return render_template('jinja/show4.jinja', userList=user_list)

# コーヒーの商品クラス
class items:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f'商品ID：{self.id} 商品名：{self.name}'

# 商品ページをfor文でを使って表示する
@app.route('/item_for')
def show_item_for():
    item_list = [items(1, 'キリマンジャロ'),items(2, 'コロンビア'),items(3, 'コスタリカ')]
    return render_template('item_for.jinja', items = item_list)

# 条件分岐
@app.route('/detail_if/<int:id>')
def show_detail_if(id):
    item_list = [items(1,'キリマンジャロ'),items(2,'コロンビア'),items(3,'コスタリカ')]
    return render_template('detail_if.jinja', show_id=id, itemList=item_list)

# エラーハンドリング：カスタム４０４ページ
@app.errorhandler(404)
def show_404_pge(error):
    msg = error.description
    print('エラー内容：', msg)
    return render_template('error/404.html'),404