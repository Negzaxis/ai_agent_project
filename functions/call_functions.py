#import
from functions.get_files_info import *
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_to_file import write_to_file
from google import genai
from google.genai import types


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,]
)

def call_function(function_call, verbose=False):
    """
    Handle calling one of the available functions and return its result.
    
    Args:
        function_call: A types.FunctionCall object with .name and .args properties
        verbose: Boolean flag to print detailed debug information
    
    Returns:
        A types.Content object containing the function response
    """
    
    # Extract function name safely as a string
    function_name = function_call.name or ""
    
    # Print function call info based on verbose mode
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")
    
    # Map function names to actual function implementations
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_to_file,
    }
    
    # Check if function name is valid
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Make a shallow copy of args, defaulting to empty dict if None
    args = dict(function_call.args) if function_call.args else {}
    
    # Set working directory to "./calculator"
    args["working_directory"] = "./calculator"
    
    # Call the appropriate function with unpacked args
    try:
        target_function = function_map[function_name]
        function_result = target_function(**args)
        
        # Return result wrapped in types.Content with from_function_response
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Error executing {function_name}: {e}"},
                )
            ],
        )