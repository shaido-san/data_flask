from flask import Flask, render_template, request

app = Flask(__name__)

#ルーティングimportの後はなんでもいい。フォームの名前だから
from forms import UserInfoForm

#ユーザ情報入力
@app.route('/', methods = ['GET','POST'])
def form_index():
    #フォームの作成
    form = UserInfoForm(request.form)
    # 入力内容に問題がない時
    if request.method == 'POST' and form.validate():
        return render_template('confirm.html', form=form)
    #入力内容に問題がある時：validatorがfalseの時
    return render_template('index.html', form=form)