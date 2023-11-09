import sqlite3
import json
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# 介面
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # 標題
        topFrame=tk.Frame(self,relief=tk.GROOVE)
        tk.Label(topFrame,text="Pokemon Sleep SQL",font=("arial",20,"bold")).pack(padx=20,pady=20,side=LEFT)
        topFrame.pack()
        
        # 新增按鈕
        self.b=ttk.Button(self,text="新增",bootstyle=DANGER)
        self.b.pack(side=LEFT,padx=5,pady=10)

        # 搜尋
        self.tree_box = ttk.LabelFrame(text="搜尋",bootstyle=DANGER)
        # 名字
        tk.Label(self.tree_box, text="名字：").pack(side=LEFT)
        search_entry = tk.Entry(self.tree_box)
        search_entry.bind("<KeyRelease>")#,self.OnEntryClick)
        search_entry.pack(side="left")
        self.tree_box.pack(fill="x",padx=10)
        self.menub1=ttk.Menubutton(text="樹果類型",bootstyle=DANGER)
        self.menub1.pack(padx=10)




def main():
    window=Window()
    window.title("Pokemon Sleep SQL")
    window.resizable(width=False,height=False)
    window.mainloop()

if __name__ == "__main__":
    main()