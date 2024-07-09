# Image to ICO Converter
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


Installing prerequisites:

pip install pillow

pip install pyinstaller

Build Windows executable:

pyinstaller --onefile --windowed --icon=app_icon.ico ico_converter.py
