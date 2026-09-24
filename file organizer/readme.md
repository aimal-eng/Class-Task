# 📁 File Organizer

A simple **Python desktop GUI application** that automatically organizes files into separate folders based on their file extensions.

The application is built using **Python, Tkinter, pathlib, and shutil**. It provides an easy-to-use graphical interface where users can select a folder and organize its files with one click.

## ✨ Features

- 📂 Select any folder using a graphical interface
- 🗂️ Automatically categorize files by type
- 📄 Organize documents
- 🖼️ Organize images
- 🎵 Organize music files
- 🎬 Organize videos
- 📦 Organize archive files
- 💻 Organize programs
- 🐍 Organize Python files
- 📊 Organize spreadsheets
- 📽️ Organize presentations
- 📁 Place unsupported file types into an `Others` folder
- 🔄 Automatically handle duplicate filenames
- 📝 Activity log showing moved files
- 🧹 Clear activity log
- ⚠️ Error and warning messages through the GUI

## 🗂️ Supported File Categories

| Category | Supported Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.svg` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv` |
| Music | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Programs | `.exe`, `.msi`, `.apk` |
| Python | `.py`, `.pyw` |
| Presentations | `.ppt`, `.pptx` |
| Spreadsheets | `.xls`, `.xlsx`, `.csv` |
| Others | Any unsupported file extension |

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** — Graphical User Interface
- **pathlib** — File and folder path management
- **shutil** — Moving files

## 📋 Requirements

Python 3.x is required.

The project uses Python's standard libraries, so no external packages are required.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/file-organizer.git
```

### 2. Open the project folder

```bash
cd file-organizer
```

### 3. Run the application

```bash
python file_organizer.py
```

On some systems, you may need:

```bash
python3 file_organizer.py
```

## 🖥️ How to Use

### Step 1 — Launch the application

Run the Python file:

```bash
python file_organizer.py
```

### Step 2 — Select a folder

Click the:

**Select Folder**

button and choose the folder containing the files you want to organize.

### Step 3 — Organize files

Click:

**▶ Organize Files**

The program will automatically create category folders and move the files into the appropriate folders.

### Example

Before organizing:

```text
MyFolder/
├── photo.jpg
├── assignment.pdf
├── song.mp3
├── movie.mp4
├── project.py
└── data.xlsx
```

After organizing:

```text
MyFolder/
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── assignment.pdf
│
├── Music/
│   └── song.mp3
│
├── Videos/
│   └── movie.mp4
│
├── Python/
│   └── project.py
│
└── Spreadsheets/
    └── data.xlsx
```

## 🔄 Duplicate Files

The application checks whether a file with the same name already exists in the destination folder.

For example:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
photo_3.jpg
```

This prevents existing files from being overwritten.

## 📝 Activity Log

The application displays an activity log showing which files were moved.

Example:

```text
Selected folder: C:/Users/User/Downloads

Moved: photo.jpg → Images
Moved: assignment.pdf → Documents
Moved: song.mp3 → Music
Moved: project.py → Python
```

The **Clear Log** button removes the displayed activity history.

## 📂 Project Structure

```text
file-organizer/
│
├── file_organizer.py
└── README.md
```

## ⚙️ How It Works

The application follows these basic steps:

```text
Select Folder
      ↓
Read Files
      ↓
Check File Extension
      ↓
Identify Category
      ↓
Create Category Folder
      ↓
Check for Duplicate Filename
      ↓
Move File
      ↓
Display Activity Log
```

The program uses a dictionary to map file extensions to categories:

```python
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".doc", ".docx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"]
}
```

The file extension is then used to determine the appropriate folder.

## 🧠 Key Python Concepts Used

This project demonstrates several important Python concepts:

- Functions
- Dictionaries
- Lists
- Loops
- Conditional statements
- Exception handling
- File handling
- Object-oriented GUI programming with Tkinter
- `pathlib.Path`
- `shutil.move()`
- String formatting
- GUI event handling

## 🔒 Safety

The application moves files from the selected folder into category folders.

It does **not** delete files.

However, because the program changes file locations, it is recommended to test it with a sample folder containing copies of your files before using it on important data.

## 🚧 Future Improvements

Possible improvements for future versions include:

- 🔍 Preview files before organizing
- ↩️ Undo the last organization
- 📊 Display the number of files in each category
- 🎨 Improve the GUI design
- 🌙 Add dark mode
- ⚙️ Allow users to create custom categories
- 🔧 Allow users to add custom file extensions
- 📅 Organize files by date
- 🔎 Add a search feature
- 📦 Create a standalone `.exe` application
- 🖱️ Add drag-and-drop support

## 📌 Project Status

**Current Status: Functional / Initial Version**

The core file-organizing functionality and graphical interface are implemented. Additional features and UI improvements can be added in future versions.

## 👨‍💻 Author

**Aimal Khan**

Built as a Python project to practice file handling, GUI development, and problem-solving.

## ⭐ Contributing

Contributions and suggestions are welcome.

If you have an idea for improving the project, feel free to open an issue or submit a pull request.

## 📄 License

This project is available for educational and personal use.
