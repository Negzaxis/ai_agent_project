import os


def write_to_file(working_directory, file_path, content):
    """
    Write content to a file within the working directory.
    
    Args:
        working_directory: The base working directory path
        file_path: The path to the file to write (relative to working_directory)
        content: The content to write to the file
    
    Returns:
        A success message if the write was successful,
        or an error message if the file_path is invalid or outside the working directory
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Validate that the file is within the working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Check if the path is a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Create parent directories if they don't exist
        parent_dir = os.path.dirname(target_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        
        # Write the content to the file
        with open(target_file, 'w') as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"