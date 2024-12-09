from flask import Flask
from flask import render_template

#インスタンス作成
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/item')
def item():
    return render_template('item.html')

@app.route('/item/<value>')
def item_detail(value):
    return render_template('item.html', value=value)