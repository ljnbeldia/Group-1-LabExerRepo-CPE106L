import tkinter as tk
from tkinter import filedialog, scrolledtext
import os

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        file_name = os.path.basename(file_path)
        file_label.config(text=f"Opened file: {file_name}")

root = tk.Tk()
root.title("Text File Viewer")

file_label = tk.Label(root, text="No file opened")
file_label.pack(pady=(10, 0))

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

open_button = tk.Button(root, text="Open Text File", command=open_file)
open_button.pack(pady=10)

root.mainloop()