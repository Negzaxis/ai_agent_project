from functions.write_to_file import write_to_file

# Test case 1: Write to existing file in calculator directory
print('Test 1: write_to_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
result = write_to_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f"Result: {result}\n")

# Test case 2: Write to new file in pkg subdirectory
print('Test 2: write_to_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
result = write_to_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f"Result: {result}\n")

# Test case 3: Attempt to write outside working directory
print('Test 3: write_to_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
result = write_to_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f"Result: {result}\n")
