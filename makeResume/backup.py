import os
import shutil

backup_dir = 'backupFiles'
source_file = 'utsavChaudhary.json'

absolute_backup_dir = os.path.abspath(backup_dir)

if os.path.exists(absolute_backup_dir):
    file_list = [name for name in os.listdir(absolute_backup_dir) if os.path.isfile(os.path.join(absolute_backup_dir, name))]
    file_count = len(file_list)
    
    print(f"Number of files in '{backup_dir}': {file_count}")
    formatted_count = f"{file_count:02}"
    new_backup_file = f"{formatted_count}_backup.json"
    new_backup_file_path = os.path.join(absolute_backup_dir, new_backup_file)
    shutil.copyfile(source_file, new_backup_file_path)
    
    print(f"Copied '{source_file}' to '{new_backup_file_path}'")
else:
    print(f"The directory '{backup_dir}' does not exist.")
