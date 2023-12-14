# ...（前面的程式碼保持不變）

# 取y值
y = pokemon_data.iloc[
    list(range(0, 5)) + list(range(15, 20)) + list(range(33, 36)) +
    list(range(52, 58)) + list(range(75, 79)) + list(range(81, 84)), 3
]

# 取X值
X = pokemon_data.iloc[
    list(range(0, 5)) + list(range(15, 20)) + list(range(33, 36)) +
    list(range(52, 58)) + list(range(75, 79)) + list(range(81, 84)),
    [5, 7, 9, 11] + list(range(13, 31))
]

# 對 skill_main 進行 Label Encoding
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
X['skill_main_encoded'] = label_encoder.fit_transform(X['skill_main'])

# 除去原始的 skill_main 欄位
X = X.drop('skill_main', axis=1)

# 繼續對其他類別型欄位做 One-Hot Encoding
categorical_columns = ['skill_second_1', 'skill_second_2', 'skill_second_3', 'skill_second_4', 'skill_second_5', 'power_up', 'power_down']

for col in categorical_columns:
    X = pd.concat([X, pd.get_dummies(X[col], prefix=col, drop_first=True)], axis=1)
    X = X.drop(col, axis=1)

# 接下來進行訓練集和測試集的劃分，並訓練模型...
