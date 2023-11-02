import sqlite3
import json

def create_table(con: sqlite3.Connection):
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon_x (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "img_num" INTEGER,
            "x_name" TEXT,
            "x_sp" INTEGER,
            "x_expertise" TEXT,
            "x_level" INTEGER,
            "x_help_fruit" TEXT,
            "x_help_fruit_num" INTEGER,
            "x_help_ingredient_1" TEXT,
            "x_help_ingredient_num_1" INTEGER,
            "x_help_ingredient_2" TEXT,
            "x_help_ingredient_num_2" INTEGER,
            "x_help_ingredient_3" TEXT,
            "x_help_ingredient_num_3" INTEGER,
            "x_help_time" TEXT,
            "x_help_max" INTEGER,
            "x_skill_main" TEXT,
            "x_skill_main_num" REAL,
            "x_skill_main_level" INTEGER,
            "x_skill_second_1" TEXT,
            "x_skill_second_num_1" REAL,
            "x_skill_second_2" TEXT,
            "x_skill_second_num_2" REAL,
            "x_skill_second_3" TEXT,
            "x_skill_second_num_3" REAL,
            "x_skill_second_4" TEXT,
            "x_skill_second_num_4" REAL,
            "x_skill_second_5" TEXT,
            "x_skill_second_num_5" REAL,
            "x_power_up" TEXT,
            "x_power_down" TEXT
        );
    ''')
    con.commit()

def insert_data(con: sqlite3.Connection, data: list[dict]):
    cursor = con.cursor()
    for entry in data:
        keys = entry.keys()
        #不知道這段在從三小
        values = [entry[key] if key != "x_help_time" else entry[key].replace(" ", "") for key in keys]
        placeholders = ",".join(["?" for _ in keys])

        cursor.execute(f'''
            INSERT INTO pokemon_x ({",".join(keys)})
            VALUES ({placeholders});
        ''', values)
    con.commit()

con = sqlite3.connect("data.db")

with open("data.json", encoding='utf-8') as file:
    data = json.load(file)

create_table(con)
insert_data(con, data)
con.close()
