#簡易なタスク管理アプリの作成
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# ----------------------------
#Flaskに対するDBの設定
# ----------------------------
#セッションを管理するシークレットキーの設定
app.config['SECRET_KEY'] = os.urandom(24)
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
#URI:インターネット上のリソースを一意に識別するための文字列
app.config['SQLALCHEMY_DATABASE_URI'] = database
#不要なトラッキングをオフにする
#  （SQLAlchemyにはアプリで発生した変更を追跡する機能があるが、処理時の負荷が高いのでfalse推奨）
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#変数dbで、SQLAlchemyを操作する
db = SQLAlchemy(app)
#flask_migrateを使用できるようにする
Migrate(app, db)

#----------------------------
#モデル
#-------------------------
#タスク
class Task(db.Model):
    #テーブル名
    __tablename__ = 'task'

    #タスクid
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #タスク内容
    content = db.Column(db.String(200), nullable=False)
    #完了フラグ
    flg_completed = db.Column(db.Boolean, default=False)

    #表示用
    def __str__(self):
        return f'タスクID：{self.id} 内容：{self.content}'
    
   # -----------------------
    #ルーティング
    #------------------------
    #一覧
    @app.route('/')
    def index():
        #未完了タスクの取得
        uncompleted_tasks = Task.query.filter_by(flg_completed=False).all()
        #完了タスクの取得
        completed_tasks = Task.query.filter_by(flg_completed=True).all()

        return render_template('index.html', 
                                uncompleted_tasks=uncompleted_tasks,
                                completed_tasks=completed_tasks)
    
    #登録
    @app.route('/new', methods=['GET', 'POST'])
    def new_task():
        if request.method == 'POST':
            #入力内容の取得
            content = request.form['content']
            #インスタンスの作成
            task = Task(content = content)
            #登録
            db.session.add(task)
            db.session.commit()
            #一覧へ
            return redirect(url_for('index'))
        #GETだったら
        return render_template('new_task.html')
    
    #完了
    @app.route('/tasks/<int:task_id>/complete', methods=['POST'])
    def complete_task(task_id):
        #対象IDのデータを取得
        task = Task.query.get(task_id)
        #完了フラグをTrueに
        task.flg_completed = True
        db.session.commit()
        return redirect(url_for('index'))
    
    #未完了
    @app.route('/tasks/<int:task_id>/uncomplete', methods=['POST'])
    def uncompleted_task(task_id):
        #対象IDのデータを取得
        task = Task.query.get(task_id)
        #完了フラグをFalseに
        task.flg_completed = False
        db.session.commit()
        return redirect(url_for('index'))
