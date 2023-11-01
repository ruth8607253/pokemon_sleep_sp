'''
img_num = 圖鑑編號

x = 進化前
x_name = 名稱
x_sp = sp值
x_expertise = 專長積分：fruit,ingredient,skill
x_level = 等級
x_help_friut = 樹果類型積分
x_help_friut_num = 樹果加成
x_help_ingredient = 食材類型積分
x_help_ingredient_num = 食材加成
x_help_time = 幫忙間隔(/小時)積分
x_help_max = 持有上限積分

y_sp = 進化後的sp值
y_name = 名稱
y_sp = sp值
y_expertise = 專長積分
y_level = 等級
y_help_friut = 樹果類型積分
y_help_friut_num = 樹果加成
y_help_ingredient = 食材類型積分
y_help_time = 幫忙間隔(/小時)積分
y_help_max = 持有上限積分

skill_main = 主技能加成項目
skill_main_num=主技能
skill_second = 副技能加成項目積分
skill_speed = 幫忙速度項目積分
skill_up = 技能機率提升項目積分
skill_ingredient = 食材機率項目積分
skill_max = 持有上限提升項目積分
skill_exp = exp獲得量項目積分


power_up = 能力增加
power_down = 能力縮減

nature = 個性

function
b
w
'''
# 名稱 = 加成*積分
x_expertise = expertise*x_expertise
x_level = level*x_level
x_help_friut = help_friut*x_help_friut*x_help_friut_num
x_help_ingredient = help_ingredient*x_help_ingredient*x_help_ingredient_num
x_help_time = help_time*x_help_time
x_help_max = help_max*x_help_max

y_expertise = expertise*y_expertise
y_level = level*y_level
y_help_friut = help_friut*y_help_friut*y_help_friut_num
y_help_ingredient = help_ingredient*y_help_ingredient*y_help_ingredient_num
y_help_time = help_time*y_help_time
y_help_max = help_max*y_help_max



# sp
x_sp =x_expertise+x_level+x_help_friut+x_help_ingredient+x_help_time+x_help_max
x_sp =x_expertise+x_level+x_help_friut+x_help_ingredient+x_help_time+x_help_max


y=b+w


{"img_num":1,
"x_name":"妙蛙種子",
"x_sp": 388,
"x_expertise" = "f",
"x_level":5,
"x_help_friut" : "金枕果",
"x_help_friut_num" : 1,
"x_help_ingredient" : "甜甜蜜",
"x_help_ingredient_num" : 2,
"x_help_time" : 12:44,
"x_help_max" : 11,
"skill_main":"skill_ingredient",
"skill_main_num":6,
"power_up"=null,
"power_down"=null}
{"img_num":1,
"x_name":"妙蛙種子",
"x_sp": 460,
"x_expertise" = "f",
"x_level":10,
"x_help_friut" : "金枕果",
"x_help_friut_num" : 1,
"x_help_ingredient" : "甜甜蜜",
"x_help_ingredient_num" : 2,
"x_help_time" : 6:58,
"x_help_max" : 11,
"skill_main":"skill_ingredient",
"skill_main_num":6,
"power_up"="skill_main",
"power_down"="skill_exp"}

