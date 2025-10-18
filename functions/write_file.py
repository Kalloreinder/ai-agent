import os


def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(full_path)

    if not (abs_work == abs_full or abs_full.startswith(abs_work + os.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(abs_work):
            os.makedirs(file_path)
        with open(abs_full, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except ValueError as e:
        return f'Error: {e}'

        