import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(full_path)

    if not(abs_work == abs_full or abs_full.startswith(abs_work + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside of the permitted working directory.'
    
    if not os.path.exists(abs_full):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(["python", full_path] + args, timeout=30, capture_output=True)
        return_string = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

        if completed_process.returncode != 0:
            return_string += f"\nProcess exited with code {completed_process.returncode}"
        
        if not completed_process.stdout:
            return_string += "\nNo output produced."

        return return_string

    except ValueError as e:
        return f'Error: executing Python file: {e}'
    
    return 0