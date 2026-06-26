# 王嘉麟 2023141010176
# 金融工程实验 小作业2

import numpy as np

# 1. 创建5到15的一维数组
arr1 = np.arange(5, 16)
print("arr1:", arr1)

# 2. 形状(3,4)全1数组
arr2 = np.ones((3, 4))
print("arr2:\n", arr2)

# 3. 检查形状、大小、数据类型
print("arr1 shape:", arr1.shape, "size:", arr1.size, "dtype:", arr1.dtype)
print("arr2 shape:", arr2.shape, "size:", arr2.size, "dtype:", arr2.dtype)

# 4. arr1第3到第7个元素
print("arr1[2:7]:", arr1[2:7])

# 5. arr2第2行
print("arr2 row 2:", arr2[1])

# 6. arr2第2列
print("arr2 col 2:", arr2[:, 1])

# 7. arr1所有元素乘以2
print("arr1 * 2:", arr1 * 2)

# 8. arr2的转置
print("arr2 transpose:\n", arr2.T)

# 9. 两个数组相加，需要调整形状
# arr1有11个元素，arr2是(3,4)=12个元素，取arr1前12个不行，那就reshape arr1
# 先把arr1扩到12个元素再reshape成(3,4)
arr1_padded = np.append(arr1, 0).reshape(3, 4)
result = arr1_padded + arr2
print("arr1(padded) + arr2:\n", result)

# 10. arr1的平均值和标准差
print("arr1 mean:", arr1.mean())
print("arr1 std:", arr1.std())

# 11. arr2每列的总和
print("arr2 column sum:", arr2.sum(axis=0))

# 12. np.where把arr1中大于10的替换为-1
arr1_replaced = np.where(arr1 > 10, -1, arr1)
print("arr1 replaced:", arr1_replaced)

# 13. 布尔索引选取arr1中的奇数
odd_arr = arr1[arr1 % 2 != 0]
print("arr1 odd elements:", odd_arr)

# 14. 创建(3,1)数组，用广播和arr2相加
arr3 = np.array([[1], [2], [3]])
print("broadcast add:\n", arr3 + arr2)
