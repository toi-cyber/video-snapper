# 動画フレーム抽出ツール

複数の動画ファイルから最初と最後のフレーム（静止画）を自動で抽出するMac用アプリケーションです。

## 🚀 かんたんセットアップ（3ステップ）

### ステップ1: ダウンロード

#### 方法A: ZIPダウンロード（推奨）
1. このページの緑色の「**Code**」ボタンをクリック
2. 「**Download ZIP**」をクリック
3. ダウンロードしたZIPファイルをデスクトップで解凍

#### 方法B: Git Clone
```bash
cd ~/Desktop
git clone https://github.com/[ユーザー名]/video-frame-extractor.git
cd video-frame-extractor
```

### ステップ2: セットアップ

1. **ターミナルを開く**
   - Finderでフォルダを右クリック → 「フォルダに新規ターミナル」
   - または、ターミナルで `cd ~/Desktop/video-frame-extractor`

2. **セットアップスクリプトを実行**（初回のみ）
   ```bash
   ./setup.sh
   ```

### ステップ3: アプリを起動

```bash
source venv/bin/activate
python gui_app.py
```

## 📱 使い方

1. **動画フォルダを選択** - 処理したい動画が入っているフォルダを選択
2. **出力フォルダを選択** - 画像を保存したいフォルダを選択
3. **画像形式を選択** - JPEG または PNG（通常はJPEGで問題なし）
4. **処理を開始** - ボタンをクリックして処理開始

### 出力ファイル
- `動画名_head.jpg` - 最初のフレーム
- `動画名_tail.jpg` - 最後のフレーム

## 🎥 対応形式
- MP4, MOV, AVI, MKV, WMV

## 🔧 必要なもの
- Mac（macOS Monterey以降推奨）
- Python 3（未インストールの場合は[公式サイト](https://www.python.org/downloads/)から）

## 📦 スタンドアロンアプリの作成（オプション）

ダブルクリックで起動できるアプリを作成したい場合：

```bash
source venv/bin/activate
python build_app.py
```

作成されたアプリは `dist/VideoFrameExtractor.app` にあります。

## ❓ トラブルシューティング

### Python3がインストールされていない
[Python公式サイト](https://www.python.org/downloads/)からダウンロード

### Permission deniedエラー
```bash
chmod +x setup.sh
```

### アプリが起動しない
エラーを確認：
```bash
source venv/bin/activate
python gui_app.py
```

### 動画が処理されない
- 動画ファイルが破損していないか確認
- 対応形式か確認（MP4, MOV等）

## 🔒 セキュリティ
- 完全オフライン動作
- 動画データは外部に送信されません
- ローカル処理のみ

## 📝 備考
- 院内での使用を想定した設計
- 将来的に動画の一部切り出しなど機能拡張可能

---

問題が解決しない場合は、エラーメッセージのスクリーンショットと共にご連絡ください。