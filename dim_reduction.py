import pandas as pd

# 注意！！！下面这里要改为对应的Emotion，这里以anger为例
Emotion = 'Anger' 

# 替换为你的CSV文件路径
csv_file1 = 'modified_in_mask.csv'
csv_file2 = str(Emotion + '.csv') # 原始的下载数据
csv_file3 = str(Emotion + '_reduced.csv')  # 新建csv用来存降维之后的数据

# 读取第一个CSV文件
df1 = pd.read_csv(csv_file1)

# 读取第二个CSV文件
df2 = pd.read_csv(csv_file2,header=None)
df2 = df2.T # 转置

# 新建一个DataFrame来保存结果
df3 = pd.DataFrame()
df3['Emotion'] = [Emotion] * len(df2)


# 定义一个函数来处理每个Category
def process_category(category, df1, df2):
    # 从第一个CSV中获取对应Category的'Index'列数值，减去1以调整列的索引
    indices = df1[df1['Category'] == category]['Index'].tolist()
    adjusted_indices = [i - 1 for i in indices if i > 0]  # 确保索引值有效

    # 从第二个CSV中获取对应列并计算平均值
    selected_columns = df2.iloc[:, adjusted_indices]
    mean_values = selected_columns.mean(axis=1)
    
    return mean_values

# 处理每个Category并更新到df3
for category in ['Head', 'Chest', 'Belly', 'Arms', 'Hands', 'Legs']:
    df3[category] = process_category(category, df1, df2)

# 保存修改后的第三个CSV文件
df3.to_csv(csv_file3, index=False)

# 需要一点时间，不要着急～
