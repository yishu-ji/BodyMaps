这是一个naive的*根据像素对应的身体部位进行数据降维*的代码demo，主要是用矩形在图片上进行像素的分割和聚类

主要包括文件：
    1. mask_coordinate.py
    2. coordinate_transform.py
    3. dim_reduction.py
    4. in_mask.csv（来源：助教提供的matlab代码生成）
    5. Emotion.csv（来源：原始下载数据，这里只以Anger.csv为例）
    6. 本样例的划分方式.jpg

主要步骤如下：
    1. 运行**mask_coordinate.py**文件，鼠标停留图片某点，会显示该点的x和y坐标；或者点击图片上某一点，会在终端输出该点的xy坐标，mask_index（1到522乘以171）和data_index（1到50364）
    2. 运行**coordinate_transform.py**文件，请记得把最开始的**Emotion**换成**对应的情绪词**，这里会根据坐标位置对像素点进行归类（请参考**本样例的划分方式.jpg**）。这里可以*根据你自己的理解和1.中看到的坐标信息调整分类标准*。这一步完成后会新增一个**modified_in_mask.csv**文件，保存了各个像素点对应的部位label（arms，legs...）
    3. 运行**dim_reduction.py**文件，这里会根据2.中的label，在原始的数据文件(**Emotion.csv**)找到对应的像素点，求取它们的算术平均值。这一步完成后会新增一个**Emotion_reduced.csv**文件，这个文件每一行为每个被试的数据(从上到下被试编号1，2，3...)，第一列为情绪，后几列为部位label对应的数值。这样的输出结果的格式支持直接在spss里打开并进行分析。这一步可能要花一些时间，不要着急～
