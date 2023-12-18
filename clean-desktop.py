import os, shutil

# Define folders on desktop
old_folders_folder = os.path.join(os.environ["USERPROFILE"], "Desktop", "Old Folders")
document_folder = os.path.join(os.environ["USERPROFILE"], "Desktop", "Documents")
image_folder = os.path.join(os.environ["USERPROFILE"], "Desktop", "Pictures")
pdf_folder = os.path.join(os.environ["USERPROFILE"], "Desktop", "Documents", "PDFs")
code_folder = os.path.join(os.environ["USERPROFILE"], "Desktop", "Documents", "Code")
other_folder = os.path.join(os.environ["USERPROFILE"], "Desktop", "Other")

# Loop through all files on the desktop
for filename in os.listdir(os.path.join(os.environ["USERPROFILE"], "Desktop")):
    filepath = os.path.join(os.environ["USERPROFILE"], "Desktop", filename)

    # Check if file starts with "."
    if filename.startswith("."):
        # Delete files starting with "."
        os.system(f"del {filepath}")
    else:
        # Get file extension
        is_folder = os.path.isdir(filepath)

        if is_folder:
            # Move folders to Old Folders
            os.makedirs(old_folders_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(old_folders_folder, filename))
        else:
            # Check file extension and move files
            extension = os.path.splitext(filename)[1]
            if extension in (".txt", ".docx"):
                os.makedirs(document_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(document_folder, filename))
            elif extension in (".jpg", ".png", ".gif"):
                os.makedirs(image_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(image_folder, filename))
            elif extension in (".pdf"):
                os.makedirs(pdf_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(pdf_folder, filename))
            elif extension in (".py", ".go", ".cpp", ".cs"):
                os.makedirs(code_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(code_folder, filename))
            else:
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(other_folder, filename))

print("Desktop cleaned up successfully!")
