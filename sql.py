import requests
import sqlite3

# 創建資料庫
def __create_table(conn:sqlite3.Connection):    
    cursor = con.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS pokemon_x(
            "id"	INTEGER,
            "x_name"	TEXT,
            "x_sp"	INTEGER,
            "x_expertise"	TEXT,
            "x_level"	INTEGER,
            "x_help_friut"	TEXT,
            "x_help_ingredient"	TEXT,
            "x_help_ingredient_num"	INTEGER,
            "x_help_time" STRFTIME('%H:%M'),
            "x_help_max"	INTEGER,
            "skill_main"	INTEGER,
            "skill_main_num" INTERGER,
            "power_up" TEXT,
            "power_down" TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        '''
    )
    con.commit()