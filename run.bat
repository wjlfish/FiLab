@echo off
chcp 65001 >nul
REM 一键运行所有作业 (Windows)
REM 用法: 双击运行 或 cmd中执行 run.bat
cd /d "%~dp0"

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
python install_deps.py

echo [3/3] 开始运行作业
echo.

echo ----------------------------------------
echo ^>^>^> 运行: 小作业1 Python基础
echo ----------------------------------------
python Works\Work1\hw1.py
echo.
echo 按回车继续下一个作业...
pause >nul

echo ----------------------------------------
echo ^>^>^> 运行: 小作业2 NumPy
echo ----------------------------------------
python Works\Work2\hw2.py
echo.
echo 按回车继续下一个作业...
pause >nul

echo ----------------------------------------
echo ^>^>^> 运行: 小作业3 Pandas
echo ----------------------------------------
python Works\Work3\hw3.py
echo.
echo 按回车继续下一个作业...
pause >nul

echo ----------------------------------------
echo ^>^>^> 运行: 小作业4 金融时间序列
echo ----------------------------------------
python Works\Work4\hw4.py
echo.
echo 按回车继续下一个作业...
pause >nul

echo ----------------------------------------
echo ^>^>^> 运行: 小作业5 Titanic分类
echo ----------------------------------------
python Works\Work5\hw5.py
echo.
echo 按回车继续下一个作业...
pause >nul

echo ----------------------------------------
echo ^>^>^> 运行: 小作业6 房价预测
echo ----------------------------------------
python Works\Work6\hw6.py
echo.
echo 按回车继续下一个作业...
pause >nul

echo ----------------------------------------
echo ^>^>^> 运行: 小作业7 非监督学习
echo ----------------------------------------
python Works\Work7\hw7.py
echo.

echo ========================================
echo 全部小作业运行完毕！
echo ========================================
echo.
echo ^>^>^> 导出大作业 Notebook 为 HTML...
jupyter nbconvert --to html Works\FinalWork1\analysis.ipynb --output analysis.html
jupyter nbconvert --to html Works\FinalWork2\research.ipynb --output research.html
echo.
echo 大作业已导出完成，是否在浏览器中打开查看？
echo 按回车打开，或直接关闭窗口跳过。
pause >nul
start "" "Works\FinalWork1\analysis.html"
start "" "Works\FinalWork2\research.html"
echo.
echo 已在浏览器中打开大作业报告。
pause
