import os
import shutil

# Define the folder path
source_folder = r"C:\Practice\python\class-mod"

# Define the subfolder names and corresponding file extensions
folders = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".txt", ".pdf", ".docx", ".xlsx", ".pptx", ".csv"],
    "archives": [".zip", ".tar", ".rar", ".gz"]
}

def organize_files():
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder {source_folder} does not exist!")
        return
    
    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Determine the destination folder based on the file extension
        destination_folder = None
        for folder, extensions in folders.items():
            if file_extension in extensions:
                destination_folder = os.path.join(source_folder, folder)
                break
        
        # If a folder for the file type was found, move the file
        if destination_folder:
            # Create the folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            # Move the file
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {destination_folder}")

if __name__ == "__main__":
    organize_files()
