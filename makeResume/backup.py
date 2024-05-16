import os
backup_dir = 'backupFiles'

absolute_backup_dir = os.path.abspath(backup_dir)
if os.path.exists(absolute_backup_dir):
    file_list = [name for name in os.listdir(absolute_backup_dir) if os.path.isfile(os.path.join(absolute_backup_dir, name))]
    file_count = len(file_list)
    
    print(f"Number of files in '{backup_dir}': {file_count}")
else:
    print(f"The directory '{backup_dir}' does not exist.")


# import os
# backup_dir = 'backupFiles'

# absolute_backup_dir = os.path.abspath(backup_dir)
# if os.path.exists(absolute_backup_dir):
#     file_list = [name for name in os.listdir(absolute_backup_dir) if os.path.isfile(os.path.join(absolute_backup_dir, name))]
#     file_count = len(file_list)
    
#     print(f"Number of files in '{backup_dir}': {file_count}")
# else:
#     print(f"The directory '{backup_dir}' does not exist.")


# after scanning the dir, copy utsavChaudhary.json in the backup_dir as #{len(fileList)}