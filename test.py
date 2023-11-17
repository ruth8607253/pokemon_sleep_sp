
當然，你可以使用 Radiobutton 來實現類似的功能，這樣可以讓使用者從多個選項中選擇一個主技能。

以下是修改後的程式碼，使用 Radiobutton 實現：

python
Copy code
skill_main_box = ttk.LabelFrame(self, text="主技能", style="WARNING")
skill_main_box.pack(fill="x", padx=(10, 10), pady=10)

sm = tk.StringVar()
skill_main_values = (
    '01 持有上限', '02 幫忙速度', '03 食物機率提升', '04 技能機率提升', '05 技能等級提升',
    '06 樹果數量', '07 櫻子果', '08 零餘果', '09 勿花果', '10 椰木果',
    '11 芒芒果', '12 木子果', '13 文柚果', '14 墨莓果', '15 番荔果',
    '16 異奇果', '17 靛莓果', '18 桃桃果'
)

def set_skill(value):
    sm.set(value)

tk.Label(skill_main_box, text="個體加成：").pack(side=tk.LEFT)

for skill in skill_main_values:
    ttk.Radiobutton(skill_main_box, text=skill, variable=sm, value=skill, style="WARNING", command=lambda val=skill: set_skill(val)).pack()

# 初始選擇第一個主技能
sm.set(skill_main_values[0])