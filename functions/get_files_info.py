import os

def get_files_info(working_directory, directory="."):
    """
    Get information about files and directories in the target directory.
    
    Args:
        working_directory: The directory path to convert to absolute
        directory: Additional directory to append (optional, default is ".")
    
    Returns:
        A formatted string listing the contents of the target directory,
        or an error message if the directory is invalid or outside the working directory
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        # Iterate over items in target directory and build output
        result = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            result.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"

