import PyInstaller.__main__
import os
import shutil
from pathlib import Path


def clean_build_dirs():
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
    
    spec_files = Path('.').glob('*.spec')
    for spec_file in spec_files:
        spec_file.unlink()


def build_app():
    clean_build_dirs()
    
    PyInstaller.__main__.run([
        'gui_app.py',
        '--name=VideoFrameExtractor',
        '--onefile',
        '--windowed',
        '--noconfirm',
        '--clean',
        '--add-data=frame_extractor.py:.',
        '--hidden-import=cv2',
        '--hidden-import=PIL',
        '--collect-all=cv2',
        '--icon=NONE',
    ])
    
    print("\\nビルド完了！")
    print("アプリケーションは dist/VideoFrameExtractor.app にあります")


if __name__ == "__main__":
    build_app()