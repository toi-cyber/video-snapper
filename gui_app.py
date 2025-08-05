import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from pathlib import Path
from frame_extractor import VideoFrameExtractor


class VideoFrameExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("動画フレーム抽出ツール")
        self.root.geometry("700x500")
        
        self.extractor = VideoFrameExtractor()
        self.input_folder = None
        self.output_folder = None
        
        self.setup_ui()
        
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        title_label = ttk.Label(main_frame, text="動画の先頭・末尾フレーム抽出", 
                               font=('Helvetica', 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=20)
        
        ttk.Label(main_frame, text="1. 動画フォルダを選択:").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.input_label = ttk.Label(main_frame, text="未選択")
        self.input_label.grid(row=1, column=1, padx=10, sticky=tk.W)
        ttk.Button(main_frame, text="フォルダを選択", 
                  command=self.select_input_folder).grid(row=1, column=2)
        
        ttk.Label(main_frame, text="2. 出力フォルダを選択:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.output_label = ttk.Label(main_frame, text="未選択")
        self.output_label.grid(row=2, column=1, padx=10, sticky=tk.W)
        ttk.Button(main_frame, text="フォルダを選択", 
                  command=self.select_output_folder).grid(row=2, column=2)
        
        ttk.Label(main_frame, text="3. 保存形式:").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.output_mode_var = tk.StringVar(value="separate")
        output_mode_frame = ttk.Frame(main_frame)
        output_mode_frame.grid(row=3, column=1, columnspan=2, sticky=tk.W)
        ttk.Radiobutton(output_mode_frame, text="動画ごとにフォルダ分け（推奨）", 
                       variable=self.output_mode_var, value="separate").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(output_mode_frame, text="全てまとめて保存", 
                       variable=self.output_mode_var, value="flat").pack(side=tk.LEFT, padx=5)
        
        ttk.Label(main_frame, text="4. 画像形式:").grid(row=4, column=0, sticky=tk.W, pady=10)
        self.format_var = tk.StringVar(value="jpg")
        format_frame = ttk.Frame(main_frame)
        format_frame.grid(row=4, column=1, columnspan=2, sticky=tk.W)
        ttk.Radiobutton(format_frame, text="JPEG", variable=self.format_var, 
                       value="jpg").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(format_frame, text="PNG", variable=self.format_var, 
                       value="png").pack(side=tk.LEFT, padx=5)
        
        self.start_button = ttk.Button(main_frame, text="処理を開始", 
                                     command=self.start_processing, state="disabled")
        self.start_button.grid(row=5, column=0, columnspan=3, pady=30)
        
        self.progress = ttk.Progressbar(main_frame, mode='determinate')
        self.progress.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        self.status_label = ttk.Label(main_frame, text="フォルダを選択してください")
        self.status_label.grid(row=7, column=0, columnspan=3, pady=5)
        
        result_frame = ttk.Frame(main_frame)
        result_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        scrollbar = ttk.Scrollbar(result_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.result_text = tk.Text(result_frame, height=10, width=80, 
                                  yscrollcommand=scrollbar.set)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.result_text.yview)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(8, weight=1)
        
    def select_input_folder(self):
        folder = filedialog.askdirectory(title="動画が入っているフォルダを選択")
        if folder:
            self.input_folder = Path(folder)
            self.input_label.config(text=folder)
            self.check_ready()
            
    def select_output_folder(self):
        folder = filedialog.askdirectory(title="画像を保存するフォルダを選択")
        if folder:
            self.output_folder = Path(folder)
            self.output_label.config(text=folder)
            self.check_ready()
            
    def check_ready(self):
        if self.input_folder and self.output_folder:
            self.start_button.config(state="normal")
            self.status_label.config(text="準備完了")
        else:
            self.start_button.config(state="disabled")
            
    def update_progress(self, current, total, filename):
        progress_percent = (current / total) * 100
        self.progress['value'] = progress_percent
        self.status_label.config(text=f"処理中: {filename} ({current}/{total})")
        
    def start_processing(self):
        self.start_button.config(state="disabled")
        self.result_text.delete(1.0, tk.END)
        self.progress['value'] = 0
        
        thread = threading.Thread(target=self.process_videos)
        thread.start()
        
    def process_videos(self):
        try:
            results = self.extractor.process_folder(
                self.input_folder,
                self.output_folder,
                self.format_var.get(),
                self.output_mode_var.get(),
                lambda c, t, f: self.root.after(0, self.update_progress, c, t, f)
            )
            
            self.root.after(0, self.show_results, results)
            
        except Exception as e:
            self.root.after(0, messagebox.showerror, "エラー", f"処理中にエラーが発生しました: {str(e)}")
            self.root.after(0, self.reset_ui)
            
    def show_results(self, results):
        self.result_text.delete(1.0, tk.END)
        
        success_count = sum(1 for _, success, _ in results if success)
        total_count = len(results)
        
        self.result_text.insert(tk.END, f"処理完了: {success_count}/{total_count} 件成功\\n\\n")
        
        for filename, success, message in results:
            status = "✓" if success else "✗"
            self.result_text.insert(tk.END, f"{status} {message}\\n")
            
        self.status_label.config(text=f"処理完了 ({success_count}/{total_count} 件成功)")
        self.progress['value'] = 100
        
        messagebox.showinfo("完了", f"処理が完了しました。\\n成功: {success_count}件\\n失敗: {total_count - success_count}件")
        self.reset_ui()
        
    def reset_ui(self):
        self.start_button.config(state="normal")


def main():
    root = tk.Tk()
    app = VideoFrameExtractorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()