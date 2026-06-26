# 金融工程实验 小作业7
# 非监督学习: K-Means聚类 + PCA降维

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 加载iris数据
iris = datasets.load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means聚类
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

print("K-Means聚类结果:")
print("聚类中心:\n", kmeans.cluster_centers_)
print("inertia:", kmeans.inertia_)

# 看看聚类和真实标签的对应
from collections import Counter
for i in range(3):
    mask = clusters == i
    print(f"Cluster {i}: {Counter(y[mask])}")

# PCA降维到2维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"\nPCA方差解释比例: {pca.explained_variance_ratio_}")
print(f"累计解释方差: {pca.explained_variance_ratio_.sum():.4f}")

# 画图: 真实标签 vs K-Means聚类
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 真实标签
scatter1 = axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="viridis", s=40)
axes[0].set_title("PCA - True Labels")
axes[0].set_xlabel("PC1")
axes[0].set_ylabel("PC2")

# 聚类结果
scatter2 = axes[1].scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap="viridis", s=40)
axes[1].set_title("PCA - KMeans Clusters")
axes[1].set_xlabel("PC1")
axes[1].set_ylabel("PC2")

plt.tight_layout()
plt.savefig("Works/Work7/fig_kmeans_pca.png", dpi=100)
plt.close()
print("\n图片已保存")
