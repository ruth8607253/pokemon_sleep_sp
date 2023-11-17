import sqlite3
import json
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.simpledialog import Dialog

# 主介面
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        # 標題----------------------------------------------
        topFrame=tk.Frame(self,relief=tk.GROOVE)
        tk.Label(topFrame,text="Pokemon Sleep SQL",font=("arial",20,"bold")).pack(padx=20,pady=(20,0),side=LEFT)
        topFrame.pack()

        # 新增按鈕-------------------------------------------
        self.b=ttk.Button(self,text="新增神奇寶貝",bootstyle=WARNING,command=self.open_NewPokemon)
        self.b.pack(side=LEFT,padx=10,pady=(0,10))

        # 搜尋-----------------------------------------------
        self.search_box = ttk.LabelFrame(text="搜尋",bootstyle=DANGER)
        self.search_box.pack(fill="x",padx=(0,10),pady=10)

        # 名字
        tk.Label(self.search_box, text="名稱：").pack(side=LEFT)
        self.search_name= ttk.Entry(self.search_box,bootstyle=DANGER)
        self.search_name.bind("<KeyRelease>",self.get_search_name)
        self.search_name.pack(side="left",pady=10)

        # 食材
        i = tk.StringVar()
        i.set("食材類型")
        ingredient_type = ttk.Menubutton(self.search_box,bootstyle=(OUTLINE,DANGER))
        ingredient_type["textvariable"] = i
        ingredient_type_values = ('01 粗枝大蔥','02 品鮮蘑菇','03 特選蛋','04 窩心洋芋','05 特選蘋果',
                                  '06 火辣香草','07 豆製肉','08 哞哞鮮奶','09 甜甜蜜','10 純粹油',
                                  '11 暖暖薑','12 好眠番茄','13 放鬆可可','14 美味尾巴','15 萌綠大豆')
        ingredient_type_menu = tk.Menu(ingredient_type, tearoff=0)
        for ingredient in ingredient_type_values:
            ingredient_type_menu.add_command(
                label=ingredient, 
                command=lambda val=ingredient: i.set(val),
                activebackground="pink"
            )
        ingredient_type["menu"] = ingredient_type_menu
        ingredient_type.pack(padx=10,pady=10, side=tk.RIGHT)

        # 樹果類型
        f = tk.StringVar()
        f.set("樹果類型")
        fruit_type = ttk.Menubutton(self.search_box,bootstyle=DANGER)
        fruit_type["textvariable"] = f
        fruit_type_values = ('01 柿仔果', '02 蘋野果','03 橙橙果','04 萄葡果','05 金枕果',
                             '06 莓莓果','07 櫻子果','08 零餘果','09 勿花果','10 椰木果',
                             '11 芒芒果','12 木子果','13 文柚果','14 墨莓果','15 番荔果',
                             '16 異奇果','17 靛莓果','18 桃桃果')
        fruit_type_menu = tk.Menu(fruit_type, tearoff=0)
        for fruit in fruit_type_values:
            fruit_type_menu.add_command(
                label=fruit, 
                command=lambda val=fruit: f.set(val),
                activebackground="pink"
            )
        fruit_type["menu"] = fruit_type_menu
        fruit_type.pack(padx=10,pady=10, side=tk.RIGHT)

        #tree view-----------------------------------------------------
        self.tree_box = ttk.LabelFrame(text="Initial Text",bootstyle=PRIMARY)
        self.tree_box.pack(fill="x",padx=(0,10),pady=10,side=LEFT)
        '''
        self.youbikeTreeView= SQL(self.tree_box,show="headings",columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack(side="left")
        vsb=ttk.Scrollbar(self.tree_box,orient="vertical",command=self.youbikeTreeView.yview)
        vsb.pack(side="left",fill="y")
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        '''

    # 把search_name引入treeview
    def get_search_name(self):
        text=self.search_name.get()
        self.tree_box.config(text=text)

    # 打開NewPokemon視窗
    def open_NewPokemon(self):
        open_window=NewPokemon()
        open_window.title("新增神奇寶貝")
        open_window.resizable(width=False,height=False)
        open_window.mainloop()

# 新增神奇寶貝介面
class NewPokemon(tk.Toplevel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        # 標題----------------------------------------------
        topFrame=tk.Frame(self,relief=tk.GROOVE)
        tk.Label(topFrame,text="新增神奇寶貝",font=("arial",20,"bold")).pack(padx=20,pady=(20,0),side=LEFT)
        topFrame.pack()

        # 基本資料---------------------------------------
        search_box = ttk.LabelFrame(self,text="基本資料",bootstyle=WARNING)
        search_box.pack(fill="x",padx=(10,10),pady=10)

        # 編號
        tk.Label(search_box, text="編號：").pack(side=LEFT)
        self.search_name= ttk.Entry(search_box,bootstyle=WARNING)
        self.search_name.bind("<KeyRelease>")
        self.search_name.pack(side="left",pady=10)

        # 名字
        tk.Label(search_box, text="名稱：").pack(side=LEFT)
        self.search_name= ttk.Entry(search_box,bootstyle=WARNING)
        self.search_name.bind("<KeyRelease>",Window.get_search_name)
        self.search_name.pack(side="left",pady=10)

        # 等級
        tk.Label(search_box, text="等級：").pack(side=LEFT)
        self.search_name= ttk.Entry(search_box,bootstyle=WARNING)
        self.search_name.bind("<KeyRelease>")
        self.search_name.pack(side="left",pady=10)

        # 幫忙能力---------------------------------------
        help_box = ttk.LabelFrame(self,text="幫忙能力",bootstyle=WARNING)
        help_box.pack(fill="x",padx=(10,10),pady=10)

        # 食材
        i = tk.StringVar()
        i.set("食材類型")
        ingredient_type = ttk.Menubutton(help_box,bootstyle=(OUTLINE,WARNING))
        ingredient_type["textvariable"] = i
        ingredient_type_values = ('01 粗枝大蔥','02 品鮮蘑菇','03 特選蛋','04 窩心洋芋','05 特選蘋果',
                                  '06 火辣香草','07 豆製肉','08 哞哞鮮奶','09 甜甜蜜','10 純粹油',
                                  '11 暖暖薑','12 好眠番茄','13 放鬆可可','14 美味尾巴','15 萌綠大豆')
        ingredient_type_menu = tk.Menu(ingredient_type, tearoff=0)
        for ingredient in ingredient_type_values:
            ingredient_type_menu.add_command(
                label=ingredient, 
                command=lambda val=ingredient: i.set(val),
                activebackground="#CDAF95"
            )
        ingredient_type["menu"] = ingredient_type_menu
        ingredient_type.pack(padx=10,pady=10, side=tk.RIGHT)

        # 樹果類型
        f = tk.StringVar()
        f.set("樹果類型")
        fruit_type = ttk.Menubutton(help_box,bootstyle=WARNING)
        fruit_type["textvariable"] = f
        fruit_type_values = ('01 柿仔果', '02 蘋野果','03 橙橙果','04 萄葡果','05 金枕果',
                             '06 莓莓果','07 櫻子果','08 零餘果','09 勿花果','10 椰木果',
                             '11 芒芒果','12 木子果','13 文柚果','14 墨莓果','15 番荔果',
                             '16 異奇果','17 靛莓果','18 桃桃果')
        fruit_type_menu = tk.Menu(fruit_type, tearoff=0)
        for fruit in fruit_type_values:
            fruit_type_menu.add_command(
                label=fruit, 
                command=lambda val=fruit: f.set(val),
                activebackground="#CDAF95"
            )
        fruit_type["menu"] = fruit_type_menu
        fruit_type.pack(padx=10,pady=10, side=tk.RIGHT)

        # 幫忙間隔
        tk.Label(help_box, text="幫忙間隔：").pack(side=LEFT)
        self.help_name= ttk.Entry(help_box,bootstyle=WARNING)
        self.help_name.bind("<KeyRelease>")
        self.help_name.pack(side="left",pady=10)

        # 持有上限
        tk.Label(help_box, text="持有上限：").pack(side=LEFT)
        self.help_name= ttk.Entry(help_box,bootstyle=WARNING)
        self.help_name.bind("<KeyRelease>")
        self.help_name.pack(side="left",pady=10)

        # 主技能---------------------------------------
        skill_main_box = ttk.LabelFrame(self, text="主技能", style="WARNING")
        skill_main_box.pack(fill="x", padx=(10, 10), pady=10)
        sm = tk.StringVar()

        skill_main_values = (
            '持有上限提升', '幫忙速度', '食物機率提升', '技能機率提升', '技能等級提升',
            '樹果數量', '幫手獎勵', '活力恢復獎勵', '夢之碎片獎勵', '研究EXP獎勵', '睡眠EXP獎勵'
        )

        def set_skill(value):
            sm.set(value)

        # 分割技能，每5个技能折行显示
        for idx, skill in enumerate(skill_main_values, start=1):
            button = ttk.Radiobutton(skill_main_box, text=skill, variable=sm, value=skill, style="WARNING", command=lambda val=skill: set_skill(val))
            button.pack(side=tk.LEFT, padx=5, pady=5)
            if idx % 5 == 0:
                skill_main_box.pack()
        sm.set(skill_main_values[0])


        # 副技能---------------------------------------
        skill_main_box = ttk.LabelFrame(self, text="主技能", style="WARNING")
        skill_main_box.pack(fill="x", padx=(10, 10), pady=10)

        selected_skills = []  # 存放已選擇的技能

        def update_selection(skill):
            if skill in selected_skills:
                selected_skills.remove(skill)
            else:
                if len(selected_skills) < 5:
                    selected_skills.append(skill)
            update_display()

        def update_display():
            for idx, skill in enumerate(skill_main_values):
                if skill in selected_skills:
                    check_buttons[idx].state(['selected'])
                else:
                    check_buttons[idx].state(['!selected'])

            skill_display.delete(0, tk.END)
            for skill in selected_skills:
                skill_display.insert(tk.END, skill)

        # 技能列表
        skill_main_values = (
            '持有上限提升', '幫忙速度', '食物機率提升', '技能機率提升', '技能等級提升',
            '樹果數量', '幫手獎勵', '活力恢復獎勵', '夢之碎片獎勵', '研究EXP獎勵', '睡眠EXP獎勵'
        )

        # 將技能選項放置到 LabelFrame 中
        tk.Label(skill_main_box, text="個體加成：").pack()

        check_buttons_frame = tk.Frame(skill_main_box)
        check_buttons_frame.pack()

        check_buttons = []
        for skill in skill_main_values:
            button = ttk.Checkbutton(check_buttons_frame, text=skill, style="WARNING", command=lambda s=skill: update_selection(s))
            button.pack(side=tk.LEFT, padx=5, pady=5)
            check_buttons.append(button)

        # 用於顯示已選擇的技能的列表
        skill_display_frame = tk.Frame(skill_main_box)
        skill_display_frame.pack()

        skill_display = tk.Listbox(skill_display_frame, width=20, height=5)
        skill_display.pack()

        # 初始設置
        update_display()



        # 儲存按鈕---------------------------------------
        save_button = ttk.Button(self, text="儲存", command=self.save_to_database,bootstyle=WARNING)
        save_button.pack(pady=10)

    def save_to_database(self):
        # Connect to the SQLite database (create one if it doesn't exist)
        conn = sqlite3.connect("pokemon_database.db")
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pokemon (
                name TEXT,
                ingredient_type TEXT,
                fruit_type TEXT,
                help_interval INTEGER
            )
        ''')

        # Get data from the entries
        name = self.search_name.get()
        ingredient_type = self.ingredient_type_var.get()
        fruit_type = self.fruit_type_var.get()
        help_interval = int(self.help_name.get()) if self.help_name.get().isdigit() else 0

        # Insert data into the database
        cursor.execute('''
            INSERT INTO pokemon (name, ingredient_type, fruit_type, help_interval)
            VALUES (?, ?, ?, ?)
        ''', (name, ingredient_type, fruit_type, help_interval))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        # Optionally, you can show a message or perform other actions after saving to the database
        print("Data saved to the database!")

if __name__ == "__main__":
    window=Window()
    window.title("Pokemon Sleep SQL")
    window.resizable(width=False,height=False)
    window.mainloop()
