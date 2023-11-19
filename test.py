# 新增神奇寶貝介面
class NewPokemon(tk.Toplevel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 標題----------------------------------------------
        topFrame = tk.Frame(self, relief=tk.GROOVE)
        tk.Label(topFrame, text="新增神奇寶貝", font=("arial", 20, "bold")).pack(padx=20, pady=(20, 0), side=tk.LEFT)
        topFrame.pack()

        # 基本資料---------------------------------------
        search_box = ttk.LabelFrame(self, text="基本資料", style="WARNING")
        search_box.pack(fill="x", padx=(10, 10), pady=10)

        # 編號
        tk.Label(search_box, text="編號：").pack(side=tk.LEFT)
        self.img_num = ttk.Entry(search_box, style="WARNING", width=5)
        self.img_num.bind("<KeyRelease>", self.save_to_database)
        self.img_num.pack(side="left", pady=10)

        # 其他部分省略...
        # 以下為 save_to_database 方法的修改
        # 創造&寫入資料庫
    def save_to_database(self, event=None):
        conn = sqlite3.connect("pokemon_database.db")
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pokemon (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "img_num" INTEGER,
                "name" TEXT,
                "sp" INTEGER,
                "expertise" TEXT,
                "level" INTEGER,
                "help_fruit" TEXT,
                "help_fruit_num" INTEGER,
                "help_ingredient_1" TEXT,
                "help_ingredient_num_1" INTEGER,
                "help_ingredient_2" TEXT,
                "help_ingredient_num_2" INTEGER,
                "help_ingredient_3" TEXT,
                "help_ingredient_num_3" INTEGER,
                "help_time" TEXT,
                "help_max" INTEGER,
                "skill_main" TEXT,
                "skill_main_num" REAL,
                "skill_main_level" INTEGER,
                "skill_second_1" TEXT,
                "skill_second_num_1" REAL,
                "skill_second_2" TEXT,
                "skill_second_num_2" REAL,
                "skill_second_3" TEXT,
                "skill_second_num_3" REAL,
                "skill_second_4" TEXT,
                "skill_second_num_4" REAL,
                "skill_second_5" TEXT,
                "skill_second_num_5" REAL,
                "power_up" TEXT,
                "power_down" TEXT
            )
        ''')

        # 省略其他部分...

        cursor.execute('''
            INSERT INTO pokemon (
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
                "power_down"
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            img_num,
            name,
            sp,
            expertise,
            level,
            help_fruit,
            help_fruit_num,
            help_ingredient_1,
            help_ingredient_num_1,
            help_ingredient_2,
            help_ingredient_num_2,
            help_ingredient_3,
            help_ingredient_num_3,
            help_time,
            help_max,
            skill_main,
            skill_main_num,
            skill_main_level,
            skill_second_1,
            skill_second_num_1,
            skill_second_2,
            skill_second_num_2,
            skill_second_3,
            skill_second_num_3,
            skill_second_4,
            skill_second_num_4,
            skill_second_5,
            skill_second_num_5,
            power_up,
            power_down
        ))

        conn.commit()
        conn.close()
        print("資料存入成功")
