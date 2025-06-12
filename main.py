import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    prompt = sys.argv

    if len(prompt) < 2:
        raise Exception("Please provide a prompt")
        #sys.exit()

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001', contents=prompt
    )

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(f"{response.text}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}\n")

main()