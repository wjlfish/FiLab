#!/bin/bash
# 一键运行所有作业 (Mac/Linux)
# 用法: chmod +x run.sh && ./run.sh

set -e
cd "$(dirname "$0")"

echo ""
echo "========================================"
echo "  金融工程实验 课程作业验证"
echo "  王嘉麟 2023141010176"
echo "========================================"
echo ""

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "[1/3] 创建虚拟环境..."
    python3 -m venv venv
else
    echo "[1/3] 虚拟环境已存在，跳过"
fi

# 激活并安装依赖
echo "[2/3] 安装依赖..."
source venv/bin/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --quiet

echo "[3/3] 开始运行作业"
echo ""

run_hw() {
    local name=$1
    local file=$2
    echo "----------------------------------------"
    echo ">>> 运行: $name"
    echo "----------------------------------------"
    python "$file"
    echo ""
}

run_hw "小作业1 Python基础" "Works/Work1/hw1.py"
run_hw "小作业2 NumPy" "Works/Work2/hw2.py"
run_hw "小作业3 Pandas" "Works/Work3/hw3.py"
run_hw "小作业4 金融时间序列" "Works/Work4/hw4.py"
run_hw "小作业5 Titanic分类" "Works/Work5/hw5.py"
run_hw "小作业6 房价预测" "Works/Work6/hw6.py"
run_hw "小作业7 非监督学习" "Works/Work7/hw7.py"

echo "========================================"
echo "全部小作业运行完毕！"
echo ""
echo ">>> 导出大作业 Notebook 为 HTML..."
jupyter nbconvert --to html Works/FinalWork1/analysis.ipynb --output analysis.html
jupyter nbconvert --to html Works/FinalWork2/research.ipynb --output research.html
echo ""
echo "大作业已导出为 HTML，可直接浏览器打开:"
echo "  - Works/FinalWork1/analysis.html"
echo "  - Works/FinalWork2/research.html"
echo "========================================"
