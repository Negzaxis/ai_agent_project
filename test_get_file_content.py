from functions.get_file_content import get_file_content

# Test case 1: Lorem ipsum text file (testing truncation)
print('Test 1: get_file_content("calculator", "lorem.txt")')
result = get_file_content("calculator", "lorem.txt")
print(f"Content length: {len(result)}")
print(f"Truncation message present: {'[TRUNCATED]' in result}")
print(f"Result:\n{result}\n")

# Test case 2: Main.py file in calculator directory
print('Test 2: get_file_content("calculator", "main.py")')
result = get_file_content("calculator", "main.py")
print(f"Result:\n{result}\n")

# Test case 3: Calculator.py file in pkg subdirectory
print('Test 3: get_file_content("calculator", "pkg/calculator.py")')
result = get_file_content("calculator", "pkg/calculator.py")
print(f"Result:\n{result}\n")

# Test case 4: Non-existent path outside working directory
print('Test 4: get_file_content("calculator", "/bin/cat")')
result = get_file_content("calculator", "/bin/cat")
print(f"Result:\n{result}\n")

# Test case 5: Non-existent file in calculator directory
print('Test 5: get_file_content("calculator", "pkg/does_not_exist.py")')
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"Result:\n{result}\n")
