@echo off
chcp 65001 >nul
REM 一键运行所有作业 (Windows)
REM 用法: 双击运行 或 cmd中执行 run.bat

echo.
echo ========================================
echo   金融工程实验 课程作业验证
echo   王嘉麟 2023141010176
echo ========================================
echo.

REM 创建虚拟环境
if not exist "venv" (
    echo [1/3] 创建虚拟环境...
    python -m venv venv
) else (
    echo [1/3] 虚拟环境已存在，跳过
)

REM 激活并安装依赖
echo [2/3] 安装依赖...
call venv\Scripts\activate.bat
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --quiet

echo [3/3] 开始运行作业
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业1 Python基础
echo ----------------------------------------
python Works\Work1\hw1.py
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业2 NumPy
echo ----------------------------------------
python Works\Work2\hw2.py
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业3 Pandas
echo ----------------------------------------
python Works\Work3\hw3.py
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业4 金融时间序列
echo ----------------------------------------
python Works\Work4\hw4.py
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业5 Titanic分类
echo ----------------------------------------
python Works\Work5\hw5.py
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业6 房价预测
echo ----------------------------------------
python Works\Work6\hw6.py
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业7 非监督学习
echo ----------------------------------------
python Works\Work7\hw7.py
echo.

echo ========================================
echo 全部小作业运行完毕！
echo 大作业请用 Jupyter Notebook 打开:
echo   - Works\FinalWork1\analysis.ipynb
echo   - Works\FinalWork2\research.ipynb
echo.
echo 启动 Jupyter:
echo   jupyter notebook
echo ========================================
pause
