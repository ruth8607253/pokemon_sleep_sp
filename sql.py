import sqlite3
import json

#創sql table
def create_table(con: sqlite3.Connection):
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 001 (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "img_num" INTEGER,
            "001_name" TEXT,
            "001_sp" INTEGER,
            "001_expertise" TEXT,
            "001_level" INTEGER,
            "001_help_fruit" TEXT,
            "001_help_fruit_num" INTEGER,
            "001_help_ingredient_1" TEXT,
            "001_help_ingredient_num_1" INTEGER,
            "001_help_ingredient_2" TEXT,
            "001_help_ingredient_num_2" INTEGER,
            "001_help_ingredient_3" TEXT,
            "001_help_ingredient_num_3" INTEGER,
            "001_help_time" TEXT,
            "001_help_max" INTEGER,
            "001_skill_main" TEXT,
            "001_skill_main_num" REAL,
            "001_skill_main_level" INTEGER,
            "001_skill_second_1" TEXT,
            "001_skill_second_num_1" REAL,
            "001_skill_second_2" TEXT,
            "001_skill_second_num_2" REAL,
            "001_skill_second_3" TEXT,
            "001_skill_second_num_3" REAL,
            "001_skill_second_4" TEXT,
            "001_skill_second_num_4" REAL,
            "001_skill_second_5" TEXT,
            "001_skill_second_num_5" REAL,
            "001_power_up" TEXT,
            "001_power_down" TEXT
        );
    ''')
    con.commit()

# 引入資料
def insert_data(con: sqlite3.Connection, values: list[dict]):
    cursor = con.cursor()
    sql = '''
    REPLACE INTO 001(
        編號, 
        名稱, 
        sp值, 
        專長積分, 
        等級, 
        樹果, 
        樹果加成,
        食材1,食材1加成,
        食材2,食材2加成,
        食材3,食材3加成,
        幫忙間隔(小時),
        持有上限,
        主技能,主技能比例or數量,主技能等級,
        副技能1,副技能1比例or數量,
        副技能2,副技能2比例or數量,
        副技能3,副技能3比例or數量,
        副技能4,副技能4比例or數量,
        副技能5,副技能5比例or數量,
        能力增加,
        能力縮減)
    values(?, ?, ?, ?, ?, ?, ?,?,?,?,?, ?, ?, ?, ?, ?, ?,?,?,?,?, ?, ?, ?, ?, ?, ?,?,?,?,)
    '''
    cursor.execute(sql, values)
    con.commit()

con = sqlite3.connect("data.db")

with open("data.json", encoding='utf-8') as file:
    data = json.load(file)

create_table(con)
con.close()
