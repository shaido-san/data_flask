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


