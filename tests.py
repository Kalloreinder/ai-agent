from functions.get_file_content import get_file_content

print("Result Lorem Ipsum text file:")
print(get_file_content("calculator", "lorem.txt"))

print("Results from main.py in calculator folder:")
print(get_file_content("calculator", "main.py"))

print("Results from /bin/cat:")
print(get_file_content("calculator", "/bin/cat"))

print("Results from a file that does not exist:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))

print("Results from calculator.py in calculator folder:")
print(get_file_content("calculator", "pkg/calculator.py"))