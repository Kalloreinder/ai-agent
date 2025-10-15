import os

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(full_path) 

    if abs_work != abs_full:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'