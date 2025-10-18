import os

MAX_CHARS = 10_000

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(full_path) 

    if not (abs_work == abs_full or abs_full.startswith(abs_work + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_full, 'r', encoding='utf-8') as f:
            file_content = f.read(MAX_CHARS)
            if len(file_content) == MAX_CHARS:
                file_content += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content
    except ValueError as e:
        return f"Error: {e}"