# 王嘉麟 2023141010176
# 金融工程实验 小作业5
# Titanic分类预测

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

# 读取数据
train_df = pd.read_csv("Works/Work5/Titanic-train.csv")
test_df = pd.read_csv("Works/Work5/Titanic-test.csv")

# 预处理函数
def preprocess(df):
    df = df.copy()

    # 填充缺失值
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna("S")

    # 性别编码
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

    # Embarked编码
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    # 提取称谓作为特征
    df["Title"] = df["Name"].str.extract(r",\s*(\w+)\.")
    title_map = {"Mr": 0, "Miss": 1, "Mrs": 2, "Master": 3}
    df["Title"] = df["Title"].map(title_map).fillna(4)

    # 家庭人数
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    # 选取特征列
    features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare",
                "Embarked", "Title", "FamilySize", "IsAlone"]
    return df[features]

# 预处理
X_train = preprocess(train_df)
y_train = train_df["Survived"]
X_test = preprocess(test_df)
y_test = test_df["Survived"]

# 模型1: 随机森林
rf = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
rf.fit(X_train, y_train)

train_pred_rf = rf.predict(X_train)
test_pred_rf = rf.predict(X_test)
print(f"随机森林 - 训练集准确率: {accuracy_score(y_train, train_pred_rf):.4f}")
print(f"随机森林 - 测试集准确率: {accuracy_score(y_test, test_pred_rf):.4f}")

# 交叉验证
cv_scores = cross_val_score(rf, X_train, y_train, cv=5)
print(f"随机森林 - 5折交叉验证: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

# 模型2: 梯度提升
gb = GradientBoostingClassifier(n_estimators=150, max_depth=4, learning_rate=0.1, random_state=42)
gb.fit(X_train, y_train)

train_pred_gb = gb.predict(X_train)
test_pred_gb = gb.predict(X_test)
print(f"\nGBDT - 训练集准确率: {accuracy_score(y_train, train_pred_gb):.4f}")
print(f"GBDT - 测试集准确率: {accuracy_score(y_test, test_pred_gb):.4f}")

cv_scores_gb = cross_val_score(gb, X_train, y_train, cv=5)
print(f"GBDT - 5折交叉验证: {cv_scores_gb.mean():.4f} (+/- {cv_scores_gb.std():.4f})")
