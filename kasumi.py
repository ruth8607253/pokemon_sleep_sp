'''
小霞：sp計算方式

假設：
寶可夢在同一個狀態下(不進化、進化1次、進化2次)，sp的function是一樣的。

模型：
未進化前，抓5對同種、但不同等級的寶可夢(共10隻)，算sp的公式 -> 套用到新的5對同種、但不同等級的寶可夢(共10隻)，看Loss值多少。
'''

# 名稱 = 加成*積分
x_expertise = expertise*x_expertise
x_level = level*x_level
x_help_friut = help_friut*x_help_friut*x_help_friut_num*x_help_friut_num
x_help_ingredient_1 = help_ingredient_1*x_help_ingredient_1*x_help_ingredient_num_1
x_help_ingredient_2 = help_ingredient_2*x_help_ingredient_2*x_help_ingredient_num_2
x_help_ingredient_3 = help_ingredient_3*x_help_ingredient_3*x_help_ingredient_num_3
x_help_time = help_time*x_help_time
x_help_max = help_max*x_help_max

skill_main=skill_main*skill_ingredient_get*x_skill_main_num*x_skill_main_level
x_skill_second_1=skill_second_1*x_skill_second_1*x_skill_second_num_1
x_skill_second_2=skill_second_2*x_skill_second_2*x_skill_second_num_2
x_skill_second_3=skill_second_3*x_skill_second_3*x_skill_second_num_3
x_skill_second_4=skill_second_4*x_skill_second_4*x_skill_second_num_4
x_skill_second_5=skill_second_5*x_skill_second_5*x_skill_second_num_5
x_power_up=power_up*x_power_up
x_power_down=power_down*x_power_down

# sp
x_sp =x_expertise+x_level+x_help_friut+x_help_ingredient+x_help_time+x_help_max
x_sp =x_expertise+x_level+x_help_friut+x_help_ingredient+x_help_time+x_help_max

import sqlite3
import json
import tkinter as tk
from tkinter import messagebox

def create_table(con: sqlite3.Connection):
    # Your create_table function code here

def insert_data(con: sqlite3.Connection, values: list[dict]):
    # Your insert_data function code here

def save_data():
    # Get data from the input fields
    data = {
        "id": id_entry.get(),
        "img_num": img_num_entry.get(),
        "001_name": name_entry.get(),
        # Add the rest of the fields here
    }

    # Insert the data into the database
    insert_data(con, [data])

    # Show a success message
    messagebox.showinfo("Success", "Data added to the database!")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Add New Table Entry")

# Create and place labels and entry fields for each column
label1 = tk.Label(root, text="ID")
label1.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

label2 = tk.Label(root, text="Image Number")
label2.grid(row=1, column=0)
img_num_entry = tk.Entry(root)
img_num_entry.grid(row=1, column=1)

label3 = tk.Label(root, text="Name")
label3.grid(row=2, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1)

# Add labels and entry fields for the remaining columns as needed

# Create a button to save the data
save_button = tk.Button(root, text="Save", command=save_data)
save_button.grid(row=3, column=0, columnspan=2)

# Initialize the SQLite database connection
con = sqlite3.connect("data.db")

# Start the Tkinter main loop
root.mainloop()

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
