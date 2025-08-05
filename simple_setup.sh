#!/bin/bash

echo "シンプルセットアップを開始します..."

# 仮想環境を作成
python3 -m venv venv

# アクティベートして最小限のパッケージをインストール
source venv/bin/activate
pip install --upgrade pip
pip install opencv-python

echo ""
echo "✅ 基本セットアップが完了しました！"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "アプリを起動するには、次のコマンドを実行してください："
echo ""
echo "  ./run_app.sh"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"