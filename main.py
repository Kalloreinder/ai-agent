import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    client = genai.Client(api_key=api_key)
    try:
        user_prompt = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
            ]
        
        response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages,
                config=types.GenerateContentConfig(system_instruction=system_prompt)
            )
        
        try:
            if sys.argv[2] == "--verbose":
                print(f"User prompt: {user_prompt}")
                print(response.text)
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        except IndexError:
            print(response.text)
    except IndexError:
        print("Error: no question was entered")
        sys.exit(1)


if __name__ == "__main__":
    main()
