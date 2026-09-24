import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import shutil




FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".svg"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx",
        ".txt", ".rtf"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi",
        ".mov", ".wmv", ".flv"
    ],

    "Music": [
        ".mp3", ".wav", ".aac",
        ".flac", ".ogg"
    ],

    "Archives": [
        ".zip", ".rar", ".7z",
        ".tar", ".gz"
    ],

    "Programs": [
        ".exe", ".msi", ".apk"
    ],

    "Python": [
        ".py", ".pyw"
    ],

    "Presentations": [
        ".ppt", ".pptx"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".csv"
    ]
}




def get_category(file_extension):

    file_extension = file_extension.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if file_extension in extensions:
            return category

    return "Others"




def get_unique_filename(destination):

    if not destination.exists():
        return destination

    counter = 1

    while True:

        new_name = (
            destination.stem
            + f"_{counter}"
            + destination.suffix
        )

        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1




def select_folder():

    folder = filedialog.askdirectory()

    if folder:

        selected_folder.set(folder)

        log_message(
            f"Selected folder: {folder}"
        )



def organize_files():

    folder = selected_folder.get()

    if not folder:

        messagebox.showwarning(
            "No Folder Selected",
            "Please select a folder first."
        )

        return

    source_folder = Path(folder)

    if not source_folder.exists():

        messagebox.showerror(
            "Error",
            "The selected folder does not exist."
        )

        return


    try:

        for file in source_folder.iterdir():

            if not file.is_file():
                continue

            if file.resolve() == Path(__file__).resolve():
                continue

            extension = file.suffix

            category = get_category(extension)

            destination_folder = source_folder / category

          
            destination_folder.mkdir(
                exist_ok=True
            )

            destination_file = (
                destination_folder / file.name
            )

            
            destination_file = get_unique_filename(
                destination_file
            )

            # Move file
            shutil.move(
                str(file),
                str(destination_file)
            )

            files_moved += 1

            log_message(
                f"Moved: {file.name} → {category}"
            )

        result_label.config(
            text=f"Successfully organized {files_moved} file(s)."
        )

        messagebox.showinfo(
            "Complete",
            f"{files_moved} file(s) organized successfully!"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{error}"
        )



def clear_log():

    log_text.delete(
        "1.0",
        tk.END
    )

    result_label.config(
        text="Ready"
    )



def log_message(message):

    log_text.insert(
        tk.END,
        message + "\n"
    )

    log_text.see(
        tk.END
    )


root = tk.Tk()

root.title("File Organizer")
root.geometry("700x500")

root.resizable(
    False,
    False
)




title_label = tk.Label(
    root,
    text="📁 File Organizer",
    font=("Arial", 24, "bold")
)

title_label.pack(
    pady=20
)



description_label = tk.Label(
    root,
    text="Automatically organize files into folders based on their type.",
    font=("Arial", 11)
)

description_label.pack(
    pady=5
)




selected_folder = tk.StringVar()

folder_frame = tk.Frame(root)

folder_frame.pack(
    pady=20
)

folder_entry = tk.Entry(
    folder_frame,
    textvariable=selected_folder,
    width=55,
    state="readonly"
)

folder_entry.grid(
    row=0,
    column=0,
    padx=5
)

select_button = tk.Button(
    folder_frame,
    text="Select Folder",
    command=select_folder,
    width=15
)

select_button.grid(
    row=0,
    column=1,
    padx=5
)



organize_button = tk.Button(
    root,
    text="▶ Organize Files",
    command=organize_files,
    width=25,
    height=2,
    font=("Arial", 12, "bold")
)

organize_button.pack(
    pady=10
)




result_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 11)
)

result_label.pack(
    pady=5
)



log_label = tk.Label(
    root,
    text="Activity Log",
    font=("Arial", 12, "bold")
)

log_label.pack(
    pady=(15, 5)
)

log_text = tk.Text(
    root,
    width=80,
    height=12
)

log_text.pack(
    padx=20
)




clear_button = tk.Button(
    root,
    text="Clear Log",
    command=clear_log,
    width=15
)

clear_button.pack(

    pady=10
)



root.mainloop()
