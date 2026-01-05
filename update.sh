#!/bin/bash

# 获取脚本所在的当前目录
cd "$(dirname "$0")"

echo "--- 正在启动利物浦赛程更新程序 ---"

# 1. 如果没有 venv 文件夹，则创建一个
if [ ! -d ".venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv .venv
fi

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 确保安装了必要的库 (每次运行检查一下，确保环境正常)
echo "正在检查依赖库..."
pip install -q requests icalendar pytz python-dotenv

# 4. 运行 Python 脚本
echo "正在获取最新比赛信息并生成日历..."
python3 football_cal.py

# 5. 自动用 Mac 日历打开生成的 .ics 文件
if [ -f "football_schedule.ics" ]; then
    echo "成功！正在导入 Mac 日历..."
    open football_schedule.ics
else
    echo "错误：未能生成 .ics 文件，请检查 API Token 或网络。"
fi

echo "--- 更新完成 ---"