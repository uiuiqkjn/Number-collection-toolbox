import os

folder_path = r" " 

def remove_yolo_from_filenames(folder_path):
    for file_name in os.listdir(folder_path):
        if '#####' in file_name:
            new_file_name = file_name.replace('#####', '###') # Replace '#####' with '###'
            
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_file_name}")

def main():
    remove_yolo_from_filenames(folder_path)

if __name__ == "__main__":
    main()
