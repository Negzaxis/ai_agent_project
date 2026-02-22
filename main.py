import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


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
args = parser.parse_args()

#store a list of our messages
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    print("Hello from ai-agent-project!")
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=messages
    )
    usage_data(response)
    print(response.text)

if __name__ == "__main__":
    main()
