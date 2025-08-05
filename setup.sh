#!/bin/bash

echo "動画フレーム抽出アプリのセットアップを開始します..."

# Python3がインストールされているか確認
if ! command -v python3 &> /dev/null; then
    echo "Python3がインストールされていません。"
    echo "https://www.python.org/downloads/ からPython3をインストールしてください。"
    exit 1
fi

# Pythonバージョンを確認
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python $PYTHON_VERSION を使用しています"

# 既存の仮想環境を削除（クリーンインストールのため）
if [ -d "venv" ]; then
    echo "既存の仮想環境を削除しています..."
    rm -rf venv
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

# インストールの確認
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ セットアップが完了しました！"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "アプリを起動するには、次のコマンドを実行してください："
    echo ""
    echo "  ./run_app.sh"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
else
    echo ""
    echo "❌ セットアップ中にエラーが発生しました。"
    echo "Python 3.9〜3.12を使用することを推奨します。"
    echo ""
    echo "それでも試してみる場合："
    echo "  ./run_app.sh"
fi