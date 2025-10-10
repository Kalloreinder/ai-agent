import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(full_path)

    if abs_work == abs_full or abs_full.startswith(abs_work + os.sep):
    
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        try:
            dir_contents = ""
            for item in os.listdir(full_path):
                item_size = os.path.getsize(os.path.join(full_path, item))
                is_dir = os.path.isdir(os.path.join(full_path,item))
                dir_contents += f"- {item}: file_size={item_size} bytes, is_dir={is_dir}\n"
            return dir_contents
        except ValueError as e:
            return f"Error: {e}"
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'