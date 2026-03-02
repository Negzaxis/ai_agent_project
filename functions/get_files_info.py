import os
from google import genai
from google.genai import types

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


#google-genai standard format to descibe a function for LLM callers: types.FunctionDeclaration
#use it to build a schema for our functions, tells the LLM how the function should be called

#first schema for get_files_info -> given to us
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

#add schema -> get_file_content
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the contents of a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to read, relative to the working directory",
            )
        },
        required=["file_path"],
    ),
)

#add schema -> run_python_file
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a Python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the Python file to run, relative to the working directory",
            )
        },
        required=["file_path"],
    ),
)

#add schema -> write_file
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or create a file with specified content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)