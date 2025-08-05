#!/bin/bash

# 仮想環境が存在するか確認
if [ ! -d "venv" ]; then
    echo "セットアップが必要です。setup.sh を実行してください。"
    exit 1
fi

# 仮想環境をアクティベートしてアプリを実行
source venv/bin/activate
python gui_app.py