import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    """
    Execute a Python file within the working directory with optional arguments.
    
    Args:
        working_directory: The base working directory path
        file_path: The path to the Python file to execute (relative to working_directory)
        args: Optional list of arguments to pass to the Python script
    
    Returns:
        A string containing the output from the script execution,
        or an error message if the file is invalid or outside the working directory
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Validate that the file is within the working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if the path is a regular file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # Check if the file ends with .py
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        # Build the command to run
        command = ["python", target_file]
        
        # Add additional arguments if provided
        if args:
            command.extend(args)
        
        # Run the subprocess with proper settings
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        
        # Build the output string
        output = ""
        
        # Check for non-zero exit code
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        
        # Check if there's any output
        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}"
        
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
