import os
# SQLAlchemyの機能をインポート
from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DBファイル作成
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')

#SQLAlchemyの機能を使ってDBに接続 echo=TrueでSQL文を表示してくれる
db_engine = create_engine(database, echo=True)
Base = declarative_base()

#
# モデルの作成(クラスの一部)
#

class Item(Base):
    #テーブル名
    __tablename__ = 'items'
    #商品ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    #商品名
    name = Column(String, nullable=False, unique=True)
    #価格
    price = Column(Integer, nullable=False,)

    #コンストラクタ
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    #表示する関数（なくてもいいけど、確認するため）
    def __str__(self):  #オブジェクトを文字列に変換する特殊メソッド
        return f'Item(商品ID:{self.id},商品名:{self.name},価格:{self.price})'

#テーブルの操作

print('(1)でテーブルを作成')
Base.metadata.create_all(db_engine)

#セッションの作成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

#削除
print('(2)データ削除：実行')
session.query(Item).delete()
session.commit()

#データ登録
print('(3)データ登録：実行')
item01 = Item('カタツムリ', 100)
item02 = Item('鹿', 2900)
item03 = Item('うし', 3000)
session.add_all([item01, item02, item03])
session.commit()

#データ参照
print('(4)データ参照全件：実行')
item_all_list = session.query(Item).order_by(Item.id).all()
for row in item_all_list:
    print(row)

#データ更新1件
print('(5)データ更新１件：実行')
target_item = session.query(Item).filter(Item.id == 1).first()
target_item.price = 600
session.commit()
target_item = session.query(Item).filter(Item.id == 1).first()
print('更新確認', target_item)

print('（６）データ更新複数件：実行')
target_item_list = session.query(Item).filter(or_(Item.id == 1, Item.id == 2)).all()
for target_item in target_item_list:
    target_item.price = 9999
session.commit()

#確認
item_all_list = session.query(Item).order_by(Item.id).all()
print('複数件更新できたか確認')
for row in item_all_list:
    print(row)
