import os
from config import MAX_FILE_READ_CHARS


def get_file_content(working_directory, file_path):
    """
    Read and return the content of a file within the working directory.
    
    Args:
        working_directory: The base working directory path
        file_path: The path to the file to read (relative to working_directory)
    
    Returns:
        The file contents as a string (limited to MAX_FILE_READ_CHARS),
        or an error message if the file is invalid or outside the working directory
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Validate that the file is within the working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if the path is a regular file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read the file content with character limit
        with open(target_file, 'r') as f:
            content = f.read(MAX_FILE_READ_CHARS)
            
            # Check if there's more content beyond the limit
            if f.read(1):
                content += f'\n[...File "{file_path}" truncated at {MAX_FILE_READ_CHARS} characters]'
        
        return content
    except Exception as e:
        return f"Error: {e}"
