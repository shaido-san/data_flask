from flask import Flask

# インスタンス作成
app = Flask(__name__)

"""
ルーティング
URLと処理を紐づける
""" 

"""
@app.route('/')
def index():
    return 'Hello World!!!fffffff!'
"""

@app.route('/')
def index():
    return '<h1>トップページ</h1>'

@app.route('/shop')
def shop():
    return '<h1>shopping</h1>'

@app.route('/shop/<value>')
def flower_val(value):
    return f'<h1>Flower!!!!!→{value}</h1>'