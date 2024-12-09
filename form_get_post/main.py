#GETとPOSTの確認
from flask import Flask, request

#インスタンス作成
app = Flask(__name__)

#GETでデータ取得
@app.route('/get')
def do_get():
    name = request.args.get('name')
    return f'こんにちは、 {name}さん'

#POSTでデータ取得(postがあったらポストでなかったらゲットを使う感じ)メソッドは小文字の時動かない場合があるから、大文字でいいと思う。
@app.route('/', methods=['GET','POST'])
def do_post():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'こんにちは、 {name}さん'
    
    return """
    <h2>POSTで送信</h2>
    <form method="POST">
        名前：<input type="text" name="name">
            <button type="submit" value="送信">送信</button>
    </form>
"""
