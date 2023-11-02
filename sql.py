import sqlite3

# 創建資料庫
def __create_table(con:sqlite3.Connection):    
    cursor = con.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS pokemon_x(
            "id"  INTEGER PRIMARY KEY,
            "img_num"	INTEGER,
            "x_name"	TEXT,
            "x_sp"	INTEGER,
            "x_expertise"	TEXT,
            "x_level"	INTEGER,
            "x_help_friut"	TEXT,
            "x_help_friut_num" INTEGER,
            "x_help_ingredient_1"	TEXT,
            "x_help_ingredient_num_1"	INTEGER,
            "x_help_ingredient_2"	TEXT,
            "x_help_ingredient_num_2"	INTEGER,
            "x_help_ingredient_3"	TEXT,
            "x_help_ingredient_num_3"	INTEGER,
            "x_help_time" TEXT,
            "x_help_max"	INTEGER,
            "x_skill_main"	INTEGER,
            "x_skill_main_num" INTEGER,
            "x_skill_main_level" INTEGER,
            "x_skill_second_1" TEXT,
            "x_skill_second_num_1" INTEGER,
            "x_skill_second_2" TEXT,
            "x_skill_second_num_2" INTEGER,
            "x_skill_second_3" TEXT,
            "x_skill_second_num_3" INTEGER,
            "x_skill_second_4" TEXT,
            "x_skill_second_num_4" INTEGER,
            "x_skill_second_5" TEXT,
            "x_skill_second_num_5" INTEGER,
            "x_power_up" TEXT,
            "x_power_down" TEXT,
        );
        '''
    )
    con.commit()

# 輸入資料庫
def __insert_data(con:sqlite3.Connection,values:list[any])->None:
    with open(data.json) as file:
        data=json.load(file)
    cursor = con.cursor()
    for entry in data:
        cursor.execute(
            '''
            INSERT INTO pokemon_x(img_num,x_name,x_sp,
            x_expertise,x_level,x_help_friut,x_help_friut_num,x_help_ingredient_1,x_help_ingredient_num_1,x_help_ingredient_2,x_help_ingredient_num_2,x_help_ingredient_3,x_help_ingredient_num_3,x_help_time,x_help_max,x_skill_main,x_skill_main_num,x_skill_main_level,x_skill_second_1,x_skill_second_num_1,x_skill_second_2,x_skill_second_num_2,x_skill_second_3,x_skill_second_num_3,x_skill_second_4,x_skill_second_num_4,x_skill_second_5,x_skill_second_num_5,x_power_up,x_power_down)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''' 
        (entry["x_expertise"], entry["x_level"], entry["x_help_friut"], entry["x_help_ingredient_num_1"], entry["x_help_ingredient_2"], entry["x_help_ingredient_num_2"], entry["x_help_ingredient_3"])
        )
    cursor.execute(sql,values)
    con.commit()

con = sqlite3.connect("data.db")
__create_table(con)
__insert_data(con)
con.close()