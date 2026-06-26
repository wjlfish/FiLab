# 金融工程实验 - 课程作业

金融工程实验课的全部作业代码和报告。

## 作业列表

### 小作业

| # | 主题 | 内容 |
|---|------|------|
| 1 | Python基础 | 数据类型、控制结构、函数 |
| 2 | NumPy | 数组操作、矩阵运算、统计计算 |
| 3 | Pandas | DataFrame操作、数据清洗、分组聚合 |
| 4 | 金融时间序列 | 双均线策略、RSI策略、收益分析 |
| 5 | 分类 | Titanic生存预测，Random Forest |
| 6 | 回归 | 房价预测，GBDT + log变换 |
| 7 | 非监督学习 | Iris数据集 K-Means聚类 + PCA降维 |

### 大作业

| # | 主题 | 内容 |
|---|------|------|
| 1 | Financial Performance Prediction | 预测上市公司季度财务指标，GBDT多目标回归，CV R2=0.83 |
| 2 | 可转债量化交易 | 多因子分析 + 策略回测，年化43%，夏普2.53 |

## 环境

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 目录结构

```
Works/
├── Work1/    # Python基础
├── Work2/    # NumPy
├── Work3/    # Pandas
├── Work4/    # 金融时间序列
├── Work5/    # 分类 Titanic
├── Work6/    # 回归 房价预测
├── Work7/    # 非监督学习
├── FinalWork1/   # Financial Performance Prediction
└── FinalWork2/   # 可转债量化交易
```
