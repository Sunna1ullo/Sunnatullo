import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Simptomlar': ['isitma, yotal', 'bosh ogrigi, kongil aynishi', 'isitma, charchoq', 'nafas qisilishi, kokrak ogrigi', 'yotal, tomoq ogrigi'],
    'Diagnostikalar': ['gripp', 'migren', 'gripp', 'yurak kasalligi', 'yotal']
}

df = pd.DataFrame(data)
df.to_csv('medical_data.csv', index=False)
print("Maʼlumotlar toʻplami muvaffaqiyatli yaratildi.")
