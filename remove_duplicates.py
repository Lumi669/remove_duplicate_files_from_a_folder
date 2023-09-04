import os
import hashlib

def calculate_hash(file_path):
    # Calculate the MD5 hash of the file
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def remove_duplicate_files(folder_path):
    # Create a dictionary to store file hashes and paths
    file_hashes = {}
    
    # Iterate through files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Calculate the hash of the file
            file_hash = calculate_hash(file_path)
            
            # If a file with the same hash already exists, remove the duplicate
            if file_hash in file_hashes:
                print(f"Removing duplicate: {file_path}")
                os.remove(file_path)
            else:
                file_hashes[file_hash] = file_path

if __name__ == "__main__":
    folder_path = "/Users/jinghuan/Desktop/170723_from_mobile"  # Replace with the path to your folder
    remove_duplicate_files(folder_path)
    print("Duplicates removed successfully.")
