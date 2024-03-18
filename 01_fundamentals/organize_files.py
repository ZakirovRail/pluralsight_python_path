import os
import shutil

desktop_path = os.path.expanduser("~/Downloads")

folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".doc", ".docs", ".docx",  ".pdf", ".txt", ".xlsx", ".csv", ".pptx", ".log"],
    "Archives": [".zip", ".rar", ".cpgz"]
}

# Create  the subfolders if they don't exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    print(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(folder_path)

# Move files to the corresponding subfolder
for file_name in os.listdir(desktop_path):
    original_file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(original_file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if file_name.endswith(extension):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    shutil.move(original_file_path, destination_folder)
