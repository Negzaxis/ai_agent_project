from functions.run_python_file import run_python_file

# Test case 1: Run calculator main.py without arguments
print('Test 1: run_python_file("calculator", "main.py")')
result = run_python_file("calculator", "main.py")
print(f"Result:\n{result}\n")

# Test case 2: Run calculator main.py with arguments
print('Test 2: run_python_file("calculator", "main.py", ["3 + 5"])')
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(f"Result:\n{result}\n")

# Test case 3: Run calculator tests
print('Test 3: run_python_file("calculator", "tests.py")')
result = run_python_file("calculator", "tests.py")
print(f"Result:\n{result}\n")

# Test case 4: Try to run file outside working directory
print('Test 4: run_python_file("calculator", "../main.py")')
result = run_python_file("calculator", "../main.py")
print(f"Result:\n{result}\n")

# Test case 5: Try to run non-existent file
print('Test 5: run_python_file("calculator", "nonexistent.py")')
result = run_python_file("calculator", "nonexistent.py")
print(f"Result:\n{result}\n")

# Test case 6: Try to run non-Python file
print('Test 6: run_python_file("calculator", "lorem.txt")')
result = run_python_file("calculator", "lorem.txt")
print(f"Result:\n{result}\n")
