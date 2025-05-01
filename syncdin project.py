import csv
import pandas as pd
import os

import tkinter as tk
from tkinter import filedialog, messagebox

# Converts a CSV file to a .cwr file (simplified formatting)
def convert_to_cwr(file_path):
    cwr_data = []  # List to hold converted rows
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cwr_row = ','.join(row)  # Simplified conversion to CWR format
            cwr_data.append(cwr_row)
    
    # Save the converted data to a .cwr file
    cwr_file_path = file_path.replace('.csv', '.cwr')
    with open(cwr_file_path, 'w') as cwrfile:
        for line in cwr_data:
            cwrfile.write(line + '\n')
    
    print(f"Converted {file_path} to {cwr_file_path}")  # Notify user of conversion
    os.startfile(f"{cwr_file_path}")  # Open the converted file

# Custom button that changes color when hovered
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]  # Store the original background color
        self.bind("<Enter>", self.on_enter)  # When mouse enters button
        self.bind("<Leave>", self.on_leave)  # When mouse leaves button

    def on_enter(self, e):
        self['background'] = '#45a049'  # Changes background on hover

    def on_leave(self, e):
        self['background'] = self.defaultBackground  # Revert to original background

# Function to open file dialog and trigger file conversion
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])  # Open file dialog for CSV files
    if file_path:
        file_label.config(text=f"Selected: {file_path}")  # Display selected file path
        status_bar.config(text="File selected - Ready")  # Update status bar
        convert_to_cwr(file_path)  # Convert the selected file to .cwr format

# --- GUI Setup ---
root = tk.Tk()
root.title("CSV File Selector")  # Set window title
root.geometry("800x600")  # Set window size
root.configure(bg="#ffffff")  # Set background color

# Frame to hold the UI elements
frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Title label at the top of the window
title_label = tk.Label(frame, text="CSV File Selector", font=("Helvetica", 24, "bold"), bg="white", fg="#2c3e50")
title_label.pack(pady=20)

# Instructional label
label = tk.Label(frame, text="Select a CSV file:", font=("Helvetica", 14), bg="white", fg="#34495e")
label.pack(pady=10)

# Browse button to trigger file selection
button = HoverButton(frame, text="Browse Files", font=("Helvetica", 12, "bold"), 
                    bg="#3498db", fg="white", padx=20, pady=10,
                    command=select_file, relief=tk.FLAT)
button.pack(pady=15)

# Label to display the selected file path
file_label = tk.Label(frame, text="No file selected", font=("Helvetica", 10), 
                      bg="#ffffff", fg="#7f8c8d", wraplength=400)
file_label.pack(pady=15)

# Status bar to show the current status at the bottom of the window
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, 
                     anchor=tk.W, bg="#ecf0f1", fg="#2c3e50",
                     font=("Helvetica", 10), padx=10, pady=5)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Start the main GUI loop
root.mainloop()
