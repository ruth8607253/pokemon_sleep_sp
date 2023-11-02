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
