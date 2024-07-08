"""
Image to ICO Converter

This program provides a graphical user interface (GUI) for converting image files (JPG, JPEG, PNG)
to ICO format, which is commonly used for Windows icons. Key features include:

1. File Selection: Users can browse and select an input image file.
2. Size Options: Users can choose to create icons with multiple standard sizes or select specific sizes.
3. Conversion: The program uses the PIL (Python Imaging Library) to convert the image to ICO format.
4. User Feedback: Success and error messages are displayed to guide the user through the process.
5. About Dialog: An 'About' option in the Help menu provides information about the application.

The GUI is built using Tkinter, making it easy to use for those unfamiliar with command-line interfaces.
This tool is particularly useful for creating custom icons for Windows applications or folders.

Author: Jamin Gray
Version: 1.0
Date: 07-08-2024
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Menu
from PIL import Image
import os

# Function to convert the image to ICO format
def convert_to_ico(input_path, output_path, sizes):
    """
    Converts the input image to ICO format with specified sizes.
    
    :param input_path: Path to the input image file
    :param output_path: Path where the output ICO file will be saved
    :param sizes: List of tuples representing the icon sizes to generate
    :return: True if conversion is successful, False otherwise
    """
    try:
        with Image.open(input_path) as img:
            # Convert image to RGBA mode if it's not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Save the image as ICO with specified sizes
            img.save(output_path, format='ICO', sizes=sizes)
        
        return True
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return False

# Function to open file dialog for selecting input image
def select_input_file():
    """
    Opens a file dialog for the user to select an input image file.
    Updates the input entry field with the selected file path.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

# Main function to handle the conversion process
def convert():
    """
    Main conversion function. Gathers all necessary information and calls convert_to_ico.
    Handles input validation and displays success/error messages.
    """
    input_path = input_entry.get()
    if not input_path:
        messagebox.showwarning("Warning", "Please select an input file.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".ico", filetypes=[("ICO files", "*.ico")])
    if not output_path:
        return

    # Determine which sizes to generate based on user selection
    sizes = []
    if all_sizes_var.get():
        sizes = [(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]
    else:
        for size, var in size_vars.items():
            if var.get():
                sizes.append((size, size))
    
    if not sizes:
        messagebox.showwarning("Warning", "Please select at least one icon size.")
        return

    # Perform the conversion and show result message
    if convert_to_ico(input_path, output_path, sizes):
        messagebox.showinfo("Success", f"Successfully converted {input_path} to {output_path}")

# Function to toggle the state of individual size checkboxes
def toggle_all_sizes():
    """
    Toggles the state of individual size checkboxes based on the 'All Sizes' checkbox.
    """
    state = tk.DISABLED if all_sizes_var.get() else tk.NORMAL
    for cb in size_checkbuttons:
        cb.config(state=state)

# Function to display the About dialog
def show_about():
    """
    Creates and displays the About dialog with application information.
    """
    about_window = tk.Toplevel(root)
    about_window.title("About Image to ICO Converter")
    about_window.geometry("300x200")
    about_window.resizable(False, False)
    
    about_text = """
    Image to ICO Converter
    Version 1.0

    This application converts JPG and PNG images
    to ICO format for use as Windows icons.

    Created using Python and Tkinter.
    Author: Jamin Gray 
    2024
    """
    
    label = tk.Label(about_window, text=about_text, justify=tk.CENTER, padx=10, pady=10)
    label.pack(expand=True)
    
    ok_button = tk.Button(about_window, text="OK", command=about_window.destroy)
    ok_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Image to ICO Converter")

# Create menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Create and place widgets for file selection
tk.Label(root, text="Input Image:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Create frame for size selection
size_frame = ttk.LabelFrame(root, text="Icon Sizes")
size_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="we")

# Add 'All Sizes' checkbox
all_sizes_var = tk.BooleanVar(value=True)
all_sizes_cb = tk.Checkbutton(size_frame, text="All Sizes", variable=all_sizes_var, command=toggle_all_sizes)
all_sizes_cb.grid(row=0, column=0, sticky="w")

# Add individual size checkboxes
size_vars = {}
size_checkbuttons = []
sizes = [16, 32, 48, 64, 128, 256]
for i, size in enumerate(sizes):
    var = tk.BooleanVar(value=False)
    size_vars[size] = var
    cb = tk.Checkbutton(size_frame, text=f"{size}x{size}", variable=var, state=tk.DISABLED)
    cb.grid(row=(i // 3) + 1, column=i % 3, sticky="w")
    size_checkbuttons.append(cb)

# Add Convert button
tk.Button(root, text="Convert", command=convert).grid(row=2, column=1, pady=10)

# Start the GUI event loop
root.mainloop()