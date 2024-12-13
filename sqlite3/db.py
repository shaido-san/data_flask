import os
import sqlite3

#DBファイル作成
base_dir = os.path.dirname(__file__)
database = os.path.join(base_dir, 'data.sqlite')

#------------------
#SQL書いていく
#------------------
#接続

connect = sqlite3.connect(database)
print('--------コネクションの接続---------')
print()

#カーソル
cursor = connect.cursor()

# テーブル削除
drop_sql = """
DROP TABLE IF EXISTS items 
"""

cursor.execute(drop_sql)
print('(1)対象テーブル(items)があれば削除')

# テーブル作成SQL
create_sql = """
CREATE TABLE items(
   item_id INTEGER PRIMARY KEY AUTOINCREMENT,
   item_name STRING UNIQUE NOT NULL,
   price INTEGER NOT NULL
)
"""

cursor.execute(create_sql)
print('(2)テーブル作成')

#データ登録SQL
insert_sql = """
   INSERT INTO items(item_name, price) VALUES(?,?)
"""
#?に値が入る
insert_data_list = [
    ('カッパえびせん',150),('カブトムシ',700),('ラーメン',800),('水',100),('コカコーラ',300)
]
cursor.executemany(insert_sql, insert_data_list)
connect.commit()
print('(3)データ登録：実行')

#データ参照（全権取得）SQL
select_all_sql = """
    SELECT * FROM items
"""

cursor.execute(select_all_sql)
data = cursor.fetchall()
print(data)
print('(4)全件取得')

# データ参照１件SQL
select_one_sql = """
    SELECT * FROM items WHERE item_id=?
"""
id = 2
cursor.execute(select_one_sql,(id,))
data = cursor.fetchall()
print(data)
print('(5)１件取得')

#データ更新SQL
updata_sql ="""
    UPDATE items SET price=? WHERE item_id=?
"""

price = 9000
id = 3
cursor.execute(updata_sql,(price,id))
connect.commit()
print('(6)データ更新：実行')
cursor.execute(select_one_sql,(id,))
data = cursor.fetchone()
print('確認用に１件表示', data)

#データ削除SQL
delete_sql ="""
     DELETE FROM items WHERE item_id=?
"""
id = 1
cursor.execute(delete_sql,(id,))
connect.commit()
print('データ削除;実行')
cursor.execute(select_all_sql)
data = cursor.fetchall()
print('確認用に全件表示:実行', data)

#閉じる（書かないとエラーが出る）
connect.close()
print('--------コネクションを閉じる---------')
