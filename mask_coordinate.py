import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

# 读取in_mask.csv文件成为dataframe
df = pd.read_csv('in_mask.csv', header=None)





def onclick(event):
    ix, iy = event.xdata, event.ydata
    # 从图片的高度中减去Y坐标
    iy_transformed = img.shape[0] - iy
    mask_index = int(iy_transformed) + int(ix) * 522
    # 在df中找到mask_index对应的data_index(如果找到了，就返回)
    if mask_index in df[0].values:
        data_index = df.loc[df[0] == mask_index].index[0]
    else:
        data_index = "Not Found"
    # data_index = df.loc[df[0] == mask_index]
    print(f'x = {ix}, y = {iy_transformed}, mask_index = {mask_index}, data_index = {data_index}')

# 替换为你的图片路径
image_path = 'mask.png'

# 读取并显示图片
img = mpimg.imread(image_path)
fig, ax = plt.subplots()
# x轴和y轴的刻度步长为50
ax.set_xticks(range(0, img.shape[1], 50))
ax.set_yticks(range(0, img.shape[0], 50))

ax.imshow(img)

# 连接事件
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

