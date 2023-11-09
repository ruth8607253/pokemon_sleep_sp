import sqlite3
import json
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# 介面
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # 標題----------------------------------------------
        topFrame=tk.Frame(self,relief=tk.GROOVE)
        tk.Label(topFrame,text="Pokemon Sleep SQL",font=("arial",20,"bold")).pack(padx=20,pady=(20,0),side=LEFT)
        topFrame.pack()
        
        # 新增按鈕-------------------------------------------
        self.b=ttk.Button(self,text="新增神奇寶貝",bootstyle=WARNING)
        self.b.pack(side=LEFT,padx=10,pady=(15,10))

        # 搜尋-----------------------------------------------
        self.tree_box = ttk.LabelFrame(text="搜尋",bootstyle=DANGER)
        self.tree_box.pack(fill="x",padx=(0,10),pady=10)
        # 名字
        tk.Label(self.tree_box, text="名字：").pack(side=LEFT)
        search_name= tk.Entry(self.tree_box,highlightbackground="pink",highlightcolor="pink")
        search_name.bind("<KeyRelease>")#,self.OnEntryClick)
        search_name.pack(side="left",pady=10)
        # 食材
        i = tk.StringVar()
        i.set("食材類型")
        ingredient_type = ttk.Menubutton(self.tree_box,bootstyle=(OUTLINE,DANGER))
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
        fruit_type = ttk.Menubutton(self.tree_box,bootstyle=DANGER)
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
        #tree view

def main():
    window=Window()
    window.title("Pokemon Sleep SQL")
    window.resizable(width=False,height=False)
    window.mainloop()

if __name__ == "__main__":
    main()