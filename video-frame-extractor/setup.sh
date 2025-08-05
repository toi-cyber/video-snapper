#!/bin/bash

echo "動画フレーム抽出アプリのセットアップを開始します..."

# Python3がインストールされているか確認
if ! command -v python3 &> /dev/null; then
    echo "Python3がインストールされていません。"
    echo "https://www.python.org/downloads/ からPython3をインストールしてください。"
    exit 1
fi

# 仮想環境を作成
echo "仮想環境を作成しています..."
python3 -m venv venv

# 仮想環境をアクティベート
echo "仮想環境をアクティベートしています..."
source venv/bin/activate

# 依存パッケージをインストール
echo "必要なパッケージをインストールしています..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "セットアップが完了しました！"
echo ""
echo "次のコマンドでアプリを実行できます:"
echo "  source venv/bin/activate"
echo "  python gui_app.py"
echo ""
echo "アプリをビルドする場合は:"
echo "  source venv/bin/activate"
echo "  python build_app.py"