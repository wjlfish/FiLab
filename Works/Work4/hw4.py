# 金融工程实验 小作业4
# 沪深300金融时间序列分析

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import akshare as ak

# 1. 数据导入
# 用akshare获取沪深300数据
df = ak.stock_zh_index_daily(symbol="sh000300")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
df = df.sort_index()
# 只取最近两年的数据，太多了画图不好看
df = df["2022-01-01":]
print(df.info())
print(df.describe())

# 2. 可视化
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# 时间序列图
axes[0].plot(df.index, df["close"], color="steelblue")
axes[0].set_title("沪深300 收盘价")
axes[0].grid(True)

# 收益柱状图
daily_ret = df["close"].pct_change().dropna()
axes[1].bar(daily_ret.index, daily_ret, color="salmon", width=1)
axes[1].set_title("沪深300 日收益率")
axes[1].grid(True)

plt.tight_layout()
plt.savefig("Works/Work4/fig1_price_and_return.png", dpi=100)
plt.close()

# 3. 汇总统计
print("\n均值:", df["close"].mean())
print("标准差:", df["close"].std())
print("最小值:", df["close"].min())
print("最大值:", df["close"].max())

# 自定义统计
custom_stats = df[["close", "volume"]].aggregate(["mean", "std", "min", "max"])
print("\n自定义统计:\n", custom_stats)

# 范围
range_val = df["close"].max() - df["close"].min()
print("价格范围:", range_val)

# 4. 时间序列变化分析
df["diff"] = df["close"].diff()
df["pct_change"] = df["close"].pct_change()
df["log_return"] = np.log(df["close"] / df["close"].shift(1))
print("\n变化分析前5行:")
print(df[["close", "diff", "pct_change", "log_return"]].head(10))

# 5. 重采样
weekly = df["close"].resample("W").last()
monthly = df["close"].resample("ME").last()
print("\n周数据前5行:\n", weekly.head())
print("\n月数据前5行:\n", monthly.head())

# 6. 滚动统计
df["ma30"] = df["close"].rolling(window=30).mean()
df["std30"] = df["close"].rolling(window=30).std()

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df.index, df["close"], label="close", alpha=0.7)
ax.plot(df.index, df["ma30"], label="MA30", color="red")
ax.fill_between(df.index, df["ma30"] - df["std30"], df["ma30"] + df["std30"],
                alpha=0.2, color="red", label="30d std band")
ax.legend()
ax.set_title("沪深300 收盘价与30日滚动均线")
ax.grid(True)
plt.tight_layout()
plt.savefig("Works/Work4/fig2_rolling.png", dpi=100)
plt.close()

# 7. 简单交易策略
# 策略1: 双均线策略 (短期10日 vs 长期30日)
df["ma10"] = df["close"].rolling(window=10).mean()
df["signal"] = 0
df.loc[df["ma10"] > df["ma30"], "signal"] = 1
df.loc[df["ma10"] <= df["ma30"], "signal"] = -1

# 策略收益
df["strategy_return"] = df["signal"].shift(1) * df["log_return"]
df["long_only_return"] = df["log_return"]

# 年化收益
trading_days = len(df["log_return"].dropna())
years = trading_days / 252

cumret_strategy = df["strategy_return"].dropna().sum()
cumret_longonly = df["long_only_return"].dropna().sum()

annual_strategy = cumret_strategy / years
annual_longonly = cumret_longonly / years
print(f"\n双均线策略年化收益: {annual_strategy:.4f}")
print(f"Long only年化收益: {annual_longonly:.4f}")

# 画累计收益对比
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df.index, df["strategy_return"].cumsum(), label="双均线策略", color="blue")
ax.plot(df.index, df["long_only_return"].cumsum(), label="Long Only", color="gray")
ax.legend()
ax.set_title("策略累计对数收益对比")
ax.grid(True)
plt.tight_layout()
plt.savefig("Works/Work4/fig3_strategy1.png", dpi=100)
plt.close()

# 策略2: RSI技术指标策略
def calc_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = (-delta).where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df["rsi"] = calc_rsi(df["close"], period=14)

# RSI策略：RSI<30买入，RSI>70卖出
df["signal2"] = 0
df.loc[df["rsi"] < 30, "signal2"] = 1
df.loc[df["rsi"] > 70, "signal2"] = -1
# 中间区域保持前一个信号
df["signal2"] = df["signal2"].replace(0, np.nan).ffill().fillna(0)

df["strategy2_return"] = df["signal2"].shift(1) * df["log_return"]

cumret_strategy2 = df["strategy2_return"].dropna().sum()
annual_strategy2 = cumret_strategy2 / years
print(f"RSI策略年化收益: {annual_strategy2:.4f}")

fig, axes = plt.subplots(2, 1, figsize=(12, 8))
axes[0].plot(df.index, df["rsi"], color="purple")
axes[0].axhline(70, color="red", linestyle="--")
axes[0].axhline(30, color="green", linestyle="--")
axes[0].set_title("RSI(14)")
axes[0].grid(True)

axes[1].plot(df.index, df["strategy2_return"].cumsum(), label="RSI策略", color="purple")
axes[1].plot(df.index, df["long_only_return"].cumsum(), label="Long Only", color="gray")
axes[1].legend()
axes[1].set_title("RSI策略 vs Long Only 累计对数收益")
axes[1].grid(True)

plt.tight_layout()
plt.savefig("Works/Work4/fig4_strategy2_rsi.png", dpi=100)
plt.close()

print("\n图片已保存到 Works/Work4/ 目录下")
