import subprocess, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('requirements.txt') as f:
    total = sum(1 for line in f if line.strip() and not line.startswith('#'))

print(f"  共 {total} 个依赖包")
print()

proc = subprocess.Popen(
    [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt',
     '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)

count = 0
for line in proc.stdout:
    if 'Collecting ' in line or 'Requirement already satisfied' in line:
        count += 1
        pct = min(int(count * 100 / total), 100)
        filled = pct // 2
        bar = '█' * filled + '░' * (50 - filled)
        print(f'\r  [{bar}] {pct}% ({count}/{total})', end='', flush=True)

print(f'\r  [{"█" * 50}] 100% ({total}/{total})')
proc.wait()

if proc.returncode == 0:
    print("  依赖安装完成！")
else:
    print("  安装过程中出现错误，请检查网络连接")
    sys.exit(1)
