import sqlite3
import numpy as np

class same_pokemon():
    def __init__(self):
        self.conn = sqlite3.connect("pokemon_database.db")
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pokemon')
        rows = cursor.fetchall()

        self.data = [np.array([row[i] for i in range(2, 16, 2)]) for row in rows]

    def get_data(self):
        return tuple(self.data)

# 創建物件
pokemon_instance = same_pokemon()
data = pokemon_instance.get_data()

# 將取得的資料分別放入變數中
name, sp, level, help_fruit_num, help_ingredient_num_1, help_ingredient_num_2, help_ingredient_num_3, help_time, help_max = data

# 現在每個變數包含了從資料庫中擷取的資料
print("name:", name)
print("sp:", sp)
print("level:", level)
print("help_fruit_num:", help_fruit_num)
print("help_ingredient_num_1:", help_ingredient_num_1)
print("help_ingredient_num_2:", help_ingredient_num_2)
print("help_ingredient_num_3:", help_ingredient_num_3)
print("help_time:", help_time)
print("help_max:", help_max)
