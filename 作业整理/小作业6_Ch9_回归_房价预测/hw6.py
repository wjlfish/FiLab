# 金融工程实验 小作业6
# 房价预测回归

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

# 读取数据
train_df = pd.read_csv("作业整理/小作业6_Ch9_回归_房价预测/house pricing/train_new.csv")
test_df = pd.read_csv("作业整理/小作业6_Ch9_回归_房价预测/house pricing/test_new.csv")

target = "SalePrice"
y_train = np.log1p(train_df[target])
y_test_raw = test_df[target]

# 合并统一处理
train_df["is_train"] = 1
test_df["is_train"] = 0
all_df = pd.concat([train_df, test_df], ignore_index=True)
all_df = all_df.drop(columns=["Id", target])

# 数值列填充中位数
num_cols = all_df.select_dtypes(include=[np.number]).columns.tolist()
num_cols.remove("is_train")
for col in num_cols:
    all_df[col] = all_df[col].fillna(all_df[col].median())

# 类别列填充并编码
cat_cols = all_df.select_dtypes(include=["object", "string"]).columns.tolist()
for col in cat_cols:
    all_df[col] = all_df[col].fillna("Missing")
    le = LabelEncoder()
    all_df[col] = le.fit_transform(all_df[col])

# 加一些交互特征
all_df["TotalSF"] = all_df["TotalBsmtSF"] + all_df["1stFlrSF"] + all_df["2ndFlrSF"]
all_df["TotalBath"] = all_df["FullBath"] + 0.5 * all_df["HalfBath"] + all_df["BsmtFullBath"] + 0.5 * all_df["BsmtHalfBath"]
all_df["Age"] = all_df["YrSold"] - all_df["YearBuilt"]
all_df["RemodAge"] = all_df["YrSold"] - all_df["YearRemodAdd"]
all_df["QualxArea"] = all_df["OverallQual"] * all_df["GrLivArea"]

# 拆回训练集和测试集
train_processed = all_df[all_df["is_train"] == 1].drop(columns=["is_train"])
test_processed = all_df[all_df["is_train"] == 0].drop(columns=["is_train"])

X_train = train_processed.values
X_test = test_processed.values

# 用log变换后的目标训练
gb = GradientBoostingRegressor(
    n_estimators=1000,
    max_depth=4,
    learning_rate=0.03,
    subsample=0.8,
    min_samples_leaf=5,
    random_state=42
)
gb.fit(X_train, y_train)

# 预测并还原
train_pred_log = gb.predict(X_train)
test_pred_log = gb.predict(X_test)

train_pred = np.expm1(train_pred_log)
test_pred = np.expm1(test_pred_log)

train_mse = mean_squared_error(np.expm1(y_train), train_pred)
test_mse = mean_squared_error(y_test_raw, test_pred)
print(f"GBDT - 训练集MSE: {train_mse:.2f}")
print(f"GBDT - 测试集MSE: {test_mse:.2f}")
print(f"GBDT - 训练集RMSE: {np.sqrt(train_mse):.2f}")
print(f"GBDT - 测试集RMSE: {np.sqrt(test_mse):.2f}")

# 交叉验证(log空间)
cv_scores = cross_val_score(gb, X_train, y_train, cv=5, scoring="neg_mean_squared_error")
cv_rmse_log = np.sqrt(-cv_scores)
print(f"GBDT - 5折CV RMSE(log): {cv_rmse_log.mean():.4f} (+/- {cv_rmse_log.std():.4f})")
