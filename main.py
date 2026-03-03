import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from functions import call_functions
from functions.call_functions import *


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("No API_Key detected.")

client = genai.Client(api_key=api_key)

# This function should get our prompt_token_count and candidates_token_count from the GenerateContentResponse object returned by the Gemini API
def usage_data(response):
    if response.usage_metadata:
        prompt_tokens = response.usage_metadata.prompt_token_count
        candidates_tokens = response.usage_metadata.candidates_token_count

        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {candidates_tokens}")
    else:
        raise RuntimeError("Usage metadata not available.")

#add the argparser
parser =argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User Prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

#store a list of our messages
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    
    # Loop for agent iterations
    max_iterations = 20
    for iteration in range(max_iterations):
        if args.verbose:
            print(f"\n--- Iteration {iteration + 1} ---")
        
        # Call the model
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0),
        )
        
        if args.verbose:
            usage_data(response)
        
        # Add candidates to conversation history
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)
        
        # Check for function calls
        function_call_list = response.function_calls or []
        function_results = []
        
        if function_call_list:
            for function_call in function_call_list:
                function_call_result = call_function(function_call, verbose=args.verbose)
                
                # Validate the response structure
                if not function_call_result.parts:
                    raise RuntimeError("Function call result has no parts")
                
                func_response = function_call_result.parts[0].function_response
                if func_response is None:
                    raise RuntimeError("Function response is None")
                
                if func_response.response is None:
                    raise RuntimeError("Function response.response is None")
                
                # Add the part to results list
                function_results.append(function_call_result.parts[0])
                
                # Print result if verbose
                if args.verbose:
                    print(f"-> {func_response.response}")
            
            # Add function results to messages for next iteration
            messages.append(types.Content(role="user", parts=function_results))
        else:
            # No function calls - model has final response
            print(response.text)
            break
    else:
        # Loop completed without break (max iterations reached)
        print("Error: Maximum iterations reached. Agent did not produce a final response.")
        exit(1)

if __name__ == "__main__":
    main()
