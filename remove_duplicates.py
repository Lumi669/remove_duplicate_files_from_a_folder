import os
import hashlib

def remove_duplicate_files(folder_path):
    # Create a dictionary to store file sizes and paths
    file_sizes = {}

    # Iterate through files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Get the size of the file
            file_size = os.path.getsize(file_path)
            
            # If a file with the same size already exists, remove the duplicate
            if file_size in file_sizes:
                print(f"Removing duplicate: {file_path}")
                os.remove(file_path)
            else:
                file_sizes[file_size] = file_path

if __name__ == "__main__":
    folder_path = "/Users/jinghuan/Desktop/170723_from_mobile"  # Replace with the path to your folder
    remove_duplicate_files(folder_path)
    print("Duplicates removed successfully.")
