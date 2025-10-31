import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    available_functions = [
        types.Tool(function_declarations=[schema_get_files_info]),
        types.Tool(function_declarations=[schema_get_file_content]),
        types.Tool(function_declarations=[schema_run_python_file]),
        types.Tool(function_declarations=[schema_write_file])
    ]
    system_prompt = """
    You are a helpul AI coding agent.
    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
    - List directories and files
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
    All paths you provide should be relative to the working directory. You do not need to specify the working directory
    in your function calls as it is automatically injected for security reasons.
    """

    client = genai.Client(api_key=api_key)
    try:
        user_prompt = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
            ]
        
        for i in range(20):
            response = client.models.generate_content(
                    model='gemini-2.0-flash-001', 
                    contents=messages,
                    config=types.GenerateContentConfig(
                        tools=available_functions,
                        system_instruction=system_prompt)
            )

            for candidate in response.candidates:
                messages.append(candidate.content)

            if response.function_calls:
                for function in response.function_calls:
                    print(f"- Calling function: {function.name}")
                    try:
                        verbose = len(sys.argv) > 2 and sys.argv[2] == '--verbose'
                        if verbose:
                            function_call_result = call_function(function, True)
                            print(f"-> {function_call_result.parts[0].function_response.response}")
                        else:
                            function_call_result = call_function(function)
                        messages.append(
                            types.Content(
                                role="user",
                                parts=[types.Part(function_response=function_call_result.parts[0].function_response)]
                                )
                            )
                    except ValueError as e:
                        print(f"Error: {e}")
            else:
                if response.text:
                    print("Final Response:")
                    print(response.text)
                    break

        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
    except IndexError:
        print("Error: no question was entered")
        sys.exit(1)


if __name__ == "__main__":
    main()
