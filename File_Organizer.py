

import os
import shutil

# Define categories and their extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mkv", ".mov", ".avi"],
}

def organize_files(directory):
    """Organize files in the given directory by type."""
    if not os.path.exists(directory):
        print("⚠️ Directory does not exist.")
        return
    
    # Create subfolders if they don’t exist
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
    
    # Create 'Others' folder
    others_path = os.path.join(directory, "Others")
    os.makedirs(others_path, exist_ok=True)
    
    # Iterate through files
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip folders
        if os.path.isdir(file_path):
            continue
        
        # Check file extension
        _, ext = os.path.splitext(filename)
        moved = False
        for category, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, category, filename))
                print(f"📂 Moved: {filename} → {category}")
                moved = True
                break
        
        if not moved:
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"📂 Moved: {filename} → Others")

    print("\n✅ File organization completed!")

# Entry point
if __name__ == "__main__":
    target_dir = input("Enter the directory path to organize: ").strip()
    organize_files(target_dir)