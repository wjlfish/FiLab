# 王嘉麟 2023141010176
# 金融工程实验 小作业3

import pandas as pd
import numpy as np

# 1. 创建DataFrame
data = {
    "name": ["张三", "李四", "王五", "赵六", "钱七"],
    "age": [21, 22, 20, 23, 21],
    "score": [88, 92, 75, 95, 83]
}
df = pd.DataFrame(data)
print(df)

# 用日期作为索引
dates = pd.date_range("2024-01-01", periods=5, freq="D")
df2 = pd.DataFrame({"value": [10, 20, 30, 40, 50]}, index=dates)
print(df2)

# 2. 数据选择和过滤
# 选单列作为Series
ages = df["age"]
print(type(ages))
print(ages)

# 布尔索引过滤
high_score = df[df["score"] > 85]
print(high_score)

# 3. 修改和添加数据
df["grade"] = ["B", "A", "C", "A", "B"]
print(df)

df["score"] = df["score"] + 5
print(df)

# 4. 聚合操作
print("mean:\n", df[["age", "score"]].mean())
print("sum:\n", df[["age", "score"]].sum())
print("max:\n", df[["age", "score"]].max())
print("min:\n", df[["age", "score"]].min())

# groupby
grouped = df.groupby("grade")["score"].mean()
print(grouped)

# 5. 合并和连接
df_a = pd.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
df_b = pd.DataFrame({"id": [4, 5, 6], "val": ["d", "e", "f"]})

# concat
df_concat = pd.concat([df_a, df_b], ignore_index=True)
print(df_concat)

# merge
df_left = pd.DataFrame({"key": [1, 2, 3], "x": [10, 20, 30]})
df_right = pd.DataFrame({"key": [2, 3, 4], "y": [200, 300, 400]})
df_merged = pd.merge(df_left, df_right, on="key")
print(df_merged)

# 6. 时间序列数据
ts_index = pd.date_range("2024-01-01", periods=30, freq="D")
ts_df = pd.DataFrame({"random_val": np.random.randn(30)}, index=ts_index)
print(ts_df.head())

# 重采样，按周取平均
weekly = ts_df.resample("W").mean()
print(weekly)
