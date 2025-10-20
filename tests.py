from functions.run_python_file import run_python_file

print("Running calculator")
print(run_python_file("calculator", "main.py"))

print("Running calculator with some addtional arguments")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Running tests in calculator folder")
print(run_python_file("calculator", "tests.py"))

print("Running main in project root dir. Should return an error")
print(run_python_file("calculator", "../main.py"))

print("Running a non-existent python file")
print(run_python_file("calculator", "nonexistent.py"))

print("Running a non-python file. Should return an error")
print(run_python_file("calculator", "lorem.txt"))
