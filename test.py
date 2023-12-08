import sqlite3
import pandas as pd

class SamePokemon():
    def __init__(self):
        self.conn = sqlite3.connect("pokemon_database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM pokemon')
        self.data = self.cursor.fetchall()

    def get_data_as_dataframe(self):
        columns = [
            "id",
            "img_num",
                "name",
                "sp",
                "expertise",
                "level",
                "help_fruit",
                "help_fruit_num",
                "help_ingredient_1",
                "help_ingredient_num_1",
                "help_ingredient_2",
                "help_ingredient_num_2",
                "help_ingredient_3",
                "help_ingredient_num_3",
                "help_time",
                "help_max",
                "skill_main",
                "skill_main_num",
                "skill_main_level",
                "skill_second_1",
                "skill_second_num_1",
                "skill_second_2",
                "skill_second_num_2",
                "skill_second_3",
                "skill_second_num_3",
                "skill_second_4",
                "skill_second_num_4",
                "skill_second_5",
                "skill_second_num_5",
                "power_up",
                "power_down","備註"
        ]

        df = pd.DataFrame(self.data, columns=columns)
        return df

# 創建一個物件
pokemon_instance = SamePokemon()

# 將資料以 DataFrame 格式讀取
pokemon_data = pokemon_instance.get_data_as_dataframe()