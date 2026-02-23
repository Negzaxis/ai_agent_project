from functions.get_files_info import get_files_info

# Test case 1: current directory
print('get_files_info("calculator", "."):\n')
result = get_files_info("calculator", ".")
print("Result for current directory:")
print(f"  {result.replace(chr(10), chr(10) + '  ')}\n")

# Test case 2: pkg subdirectory
print('get_files_info("calculator", "pkg"):\n')
result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(f"  {result.replace(chr(10), chr(10) + '  ')}\n")

# Test case 3: /bin (outside working directory)
print('get_files_info("calculator", "/bin"):\n')
result = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(f"    {result}\n")

# Test case 4: ../ (outside working directory)
print('get_files_info("calculator", "../"):\n')
result = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(f"    {result}\n")
