from functions.write_file import write_file

print("Replacing lorem.txt with some text")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("Creating new file with text in it")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("Attempting to create a file on a non-valid directory")
print(write_file("calculator", "/tmp/tempt.txt", "this should not be allowed"))
