import pandas as pd

csv_file = 'in_mask.csv'
df = pd.read_csv(csv_file,header=None)

# 定义分类函数
def classify(row):
    x, y = divmod(row, 522) # mask index / 522 的结果(x)和余数(y)分别是index的行和列
    if 0 <= x <= 32 and 0 <= y <= 260:
        return 'Arms'
    elif 139 < x <= 171 and 0 <= y <= 260:
        return 'Arms'
    elif 0 <= x <= 32 and 260 < y <= 310:
        return 'Hands'
    elif 139 < x <= 171 and 260 < y <= 310:
        return 'Hands'
    elif 32 < x <= 139 and 0 <= y <= 80:
        return 'Head'
    elif 32 < x <= 139 and 80 < y <= 200:
        return 'Chest'
    elif 32 < x <= 139 and 200 < y <= 260:
        return 'Belly'
    elif 32 < x <= 139 and 260 < y <= 522:
        return 'Legs'   
    # else:
    #     return 'Other'

# 应用分类函数
df['Category'] = df.iloc[:, 0].apply(classify)

#修改列名
df.columns = ['MaskIndex', 'Category']
# 在最左侧增加一列从1到50364的序号
df.insert(0, 'Index', range(1, 1 + len(df)))

# 保存修改后的DataFrame为新的CSV文件
df.to_csv('modified_in_mask.csv', index=False)