import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import glob

class RTFDToTXTConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RTFD and RTF to TXT Bulk Converter")
        self.create_widgets()

    def create_widgets(self):
        # Frame for File Selection
        frame_file_selection = ttk.Frame(self)
        frame_file_selection.pack(padx=10, pady=10, fill='x')

        self.label_file_selection = ttk.Label(frame_file_selection, text="No files selected")
        self.label_file_selection.pack(side=tk.LEFT, fill='x', expand=True)

        button_select_files = ttk.Button(frame_file_selection, text="Select RTFD/RTF Files", command=self.select_files)
        button_select_files.pack(side=tk.RIGHT)

        # Frame for Output Folder
        frame_output_folder = ttk.Frame(self)
        frame_output_folder.pack(padx=10, pady=10, fill='x')

        self.label_output_folder = ttk.Label(frame_output_folder, text="No output folder selected")
        self.label_output_folder.pack(side=tk.LEFT, fill='x', expand=True)

        button_output_folder = ttk.Button(frame_output_folder, text="Select Output Folder", command=self.select_output_folder)
        button_output_folder.pack(side=tk.RIGHT)

        # Convert Button
        button_convert = ttk.Button(self, text="Convert Files", command=self.convert_files)
        button_convert.pack(padx=10, pady=10)

        self.rtfd_rtf_files = []
        self.output_folder = ""

    def select_files(self):
        filetypes = [('RTFD/RTF Files', '*.rtfd'), ('RTF Files', '*.rtf')]
        filenames = filedialog.askopenfilenames(title='Select RTFD/RTF Files', filetypes=filetypes)
        if filenames:
            self.rtfd_rtf_files = filenames
            self.label_file_selection.config(text=f"{len(self.rtfd_rtf_files)} files selected")

    def select_output_folder(self):
        foldername = filedialog.askdirectory(title='Select Output Folder')
        if foldername:
            self.output_folder = foldername
            self.label_output_folder.config(text=f"Output Folder: {os.path.basename(foldername)}")

    def convert_file(self, file_path):
        try:
            file_name = os.path.basename(file_path)
            txt_filename = file_name.replace('.rtfd', '.txt')
            txt_file_path = os.path.join(self.output_folder, txt_filename)

            if file_path.endswith('.rtfd'):
                # Assuming the RTF file inside .rtfd is named 'TXT.rtf'
                rtf_file_path = os.path.join(file_path, 'TXT.rtf')
                if not os.path.exists(rtf_file_path):
                    messagebox.showerror("Error", f"No RTF file found in {file_name}")
                    return
            else:
                rtf_file_path = file_path

            # Using textutil for conversion
            subprocess.run(['textutil', '-convert', 'txt', '-output', txt_file_path, rtf_file_path])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while converting {file_name}: {e}")

    def convert_files(self):
        if not self.rtfd_rtf_files:
            messagebox.showwarning("Warning", "Please select RTFD/RTF files to convert.")
            return
        if not self.output_folder:
            messagebox.showwarning("Warning", "Please select an output folder.")
            return

        for file in self.rtfd_rtf_files:
            self.convert_file(file)

        messagebox.showinfo("Success", "All files have been converted successfully.")

if __name__ == "__main__":
    app = RTFDToTXTConverter()
    app.mainloop()
