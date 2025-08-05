import cv2
import os
from pathlib import Path
from typing import List, Tuple, Optional


class VideoFrameExtractor:
    def __init__(self):
        self.supported_formats = ['.mp4', '.mov', '.avi', '.mkv', '.wmv']
        
    def is_video_file(self, file_path: Path) -> bool:
        return file_path.suffix.lower() in self.supported_formats
    
    def extract_frames(self, video_path: Path, output_dir: Path, image_format: str = 'jpg', output_mode: str = 'separate') -> Tuple[bool, str]:
        try:
            cap = cv2.VideoCapture(str(video_path))
            
            if not cap.isOpened():
                return False, f"動画ファイルを開けませんでした: {video_path.name}"
            
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            if total_frames == 0:
                cap.release()
                return False, f"フレーム数が0です: {video_path.name}"
            
            ret, first_frame = cap.read()
            if not ret:
                cap.release()
                return False, f"最初のフレームを読み込めませんでした: {video_path.name}"
            
            base_name = video_path.stem
            
            if output_mode == 'separate':
                video_output_dir = output_dir / base_name
                video_output_dir.mkdir(exist_ok=True)
                head_filename = video_output_dir / f"start.{image_format}"
                tail_filename = video_output_dir / f"end.{image_format}"
            else:
                head_filename = output_dir / f"{base_name}_head.{image_format}"
                tail_filename = output_dir / f"{base_name}_tail.{image_format}"
            
            cv2.imwrite(str(head_filename), first_frame)
            
            cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
            ret, last_frame = cap.read()
            
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 2)
                ret, last_frame = cap.read()
            
            if ret:
                cv2.imwrite(str(tail_filename), last_frame)
            else:
                cap.release()
                return False, f"最後のフレームを読み込めませんでした: {video_path.name}"
            
            cap.release()
            return True, f"成功: {video_path.name}"
            
        except Exception as e:
            return False, f"エラーが発生しました ({video_path.name}): {str(e)}"
    
    def process_folder(self, input_folder: Path, output_folder: Path, 
                      image_format: str = 'jpg', output_mode: str = 'separate', 
                      progress_callback=None) -> List[Tuple[str, bool, str]]:
        results = []
        video_files = []
        
        for file_path in input_folder.iterdir():
            if file_path.is_file() and self.is_video_file(file_path):
                video_files.append(file_path)
        
        total_files = len(video_files)
        
        for idx, video_file in enumerate(video_files):
            success, message = self.extract_frames(video_file, output_folder, image_format, output_mode)
            results.append((video_file.name, success, message))
            
            if progress_callback:
                progress_callback(idx + 1, total_files, video_file.name)
        
        return results